import os
import uuid
import base64
from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field

from email.mime.text import MIMEText
from email.header import Header

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

from dotenv import load_dotenv

# --------------------------------------------------------------------
# LOAD ENV & CONFIG
# --------------------------------------------------------------------
load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/gmail.send",
]

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REFRESH_TOKEN = os.getenv("GOOGLE_REFRESH_TOKEN")
GOOGLE_ACCOUNT_EMAIL = os.getenv("GOOGLE_ACCOUNT_EMAIL", "your.email@gmail.com")
TIMEZONE = os.getenv("TIMEZONE", "Asia/Jakarta")
GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")


# --------------------------------------------------------------------
# GOOGLE CREDS HELPERS (NO JSON FILES)
# --------------------------------------------------------------------
def get_user_creds() -> Credentials:
    """
    Build Credentials dynamically from env vars.
    Uses refresh token + client id/secret to always get a fresh access token.
    No JSON files are used.
    """
    if not (GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET and GOOGLE_REFRESH_TOKEN):
        raise RuntimeError(
            "Missing GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET / GOOGLE_REFRESH_TOKEN in .env"
        )

    # We create a Credentials object with only refresh_token + client info.
    # token=None means we'll always refresh to get a valid access token.
    creds = Credentials(
        token=None,
        refresh_token=GOOGLE_REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        scopes=SCOPES,
    )

    try:
        creds.refresh(Request())
    except Exception as e:
        # Typically invalid_grant when refresh token is wrong or revoked
        raise RuntimeError(f"Failed to refresh access token: {e}")

    return creds


def get_calendar_service():
    creds = get_user_creds()
    return build("calendar", "v3", credentials=creds)


def get_gmail_service():
    creds = get_user_creds()
    return build("gmail", "v1", credentials=creds)


# --------------------------------------------------------------------
# MODELS
# --------------------------------------------------------------------
class SendGmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    cc: Optional[str] = None   # comma-separated list (optional)
    bcc: Optional[str] = None  # comma-separated list (optional)


class CreateCalendarEventRequest(BaseModel):
    title: str
    date: str = Field(..., description="Date in YYYY-MM-DD format")
    time: str = Field(..., description="Start time in HH:MM (24h) format")
    attendees: List[EmailStr] = []


class CreateCalendarEventResponse(BaseModel):
    event_id: str
    html_link: str
    meet_link: Optional[str] = None


# --------------------------------------------------------------------
# FASTAPI APP
# --------------------------------------------------------------------
app = FastAPI(
    title="Gmail & Calendar API (Env-only OAuth)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------
def build_mime_message(req: SendGmailRequest) -> MIMEText:
    """
    Build a MIMEText email message for Gmail API.
    """
    msg = MIMEText(req.body, "plain", "utf-8")
    msg["From"] = GOOGLE_ACCOUNT_EMAIL
    msg["To"] = req.to
    msg["Subject"] = Header(req.subject, "utf-8")

    if req.cc:
        msg["Cc"] = req.cc
    if req.bcc:
        msg["Bcc"] = req.bcc

    return msg


def parse_start_end_datetime(date_str: str, time_str: str):
    """
    Convert 'YYYY-MM-DD' + 'HH:MM' into ISO strings.
    Adds 1-hour duration.
    """
    try:
        start = datetime.fromisoformat(f"{date_str}T{time_str}:00")
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="Invalid date/time format. Use date='YYYY-MM-DD' and time='HH:MM' (24h).",
        )
    end = start + timedelta(hours=1)
    return start.isoformat(), end.isoformat()


# --------------------------------------------------------------------
# ENDPOINTS
# --------------------------------------------------------------------
@app.post("/send_gmail", response_model=str, summary="Send Gmail via Gmail API")
def send_gmail(req: SendGmailRequest):
    """
    Send an email via Gmail API using OAuth (no SMTP, no app password).
    """
    try:
        service = get_gmail_service()

        msg = build_mime_message(req)
        raw_message = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")

        message = (
            service.users()
            .messages()
            .send(userId="me", body={"raw": raw_message})
            .execute()
        )

        return f"Email sent via Gmail API. Message ID: {message.get('id')}"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post(
    "/create_calendar_event",
    response_model=CreateCalendarEventResponse,
    summary="Create Calendar Event on my Gmail calendar",
)
def create_calendar_event(req: CreateCalendarEventRequest):
    """
    Create a Google Calendar event on the OAuth user's calendar
    (GOOGLE_ACCOUNT_EMAIL), with optional attendees and Google Meet link.
    """
    try:
        service = get_calendar_service()

        start_iso, end_iso = parse_start_end_datetime(req.date, req.time)

        event = {
            "summary": req.title,
            "start": {
                "dateTime": start_iso,
                "timeZone": TIMEZONE,
            },
            "end": {
                "dateTime": end_iso,
                "timeZone": TIMEZONE,
            },
        }

        if req.attendees:
            event["attendees"] = [{"email": email} for email in req.attendees]

        # Try to create Google Meet link
        event["conferenceData"] = {
            "createRequest": {
                "requestId": str(uuid.uuid4()),
                "conferenceSolutionKey": {"type": "hangoutsMeet"},
            }
        }

        created = (
            service.events()
            .insert(
                calendarId=GOOGLE_CALENDAR_ID,
                body=event,
                conferenceDataVersion=1,
                sendUpdates="all",
            )
            .execute()
        )

        return CreateCalendarEventResponse(
            event_id=created.get("id"),
            html_link=created.get("htmlLink", ""),
            meet_link=created.get("hangoutLink"),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))