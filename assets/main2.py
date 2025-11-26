import os
import smtplib
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from email.mime.text import MIMEText
from email.header import Header

from dotenv import load_dotenv
load_dotenv() 

# ----------------- SMTP CONFIG -----------------

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = os.getenv("SMTP_EMAIL")        # your full Gmail address
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # app password from https://myaccount.google.com/apppasswords

# ----------------- FASTAPI APP -----------------

app = FastAPI(
    title="Gmail & Calendar API",
    version="1.0.0"
)

# ----------------- REQUEST MODEL -----------------

class SendGmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    cc: Optional[str] = None
    bcc: Optional[str] = None

# ----------------- HELPER -----------------

def build_mime_smtp(req: SendGmailRequest) -> MIMEText:
    msg = MIMEText(req.body, "plain", "utf-8")
    msg["From"] = SMTP_EMAIL
    msg["To"] = req.to
    msg["Subject"] = Header(req.subject, "utf-8")
    if req.cc:
        msg["Cc"] = req.cc
    if req.bcc:
        msg["Bcc"] = req.bcc
    return msg

# ----------------- ENDPOINT -----------------

@app.post("/send_gmail", response_model=str, summary="Send Gmail")
def send_gmail(req: SendGmailRequest):
    """
    Send email via Gmail SMTP using app password.
    """
    if not SMTP_EMAIL or not SMTP_PASSWORD:
        raise HTTPException(status_code=500, detail="SMTP creds not configured")

    try:
        msg = build_mime_smtp(req)

        # all recipients (to + cc + bcc)
        recipients = [req.to]
        if req.cc:
            recipients += [e.strip() for e in req.cc.split(",") if e.strip()]
        if req.bcc:
            recipients += [e.strip() for e in req.bcc.split(",") if e.strip()]

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, recipients, msg.as_string())

        return "Email sent successfully via SMTP"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
