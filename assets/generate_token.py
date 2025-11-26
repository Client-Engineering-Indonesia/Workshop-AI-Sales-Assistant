from __future__ import print_function
import os

from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv

# Scopes for Calendar events + Gmail send
SCOPES = [
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/gmail.send",
]

def main():
    load_dotenv()

    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise RuntimeError("GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET is not set in .env")

    # This mimics the usual credentials.json, but built from env
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }

    flow = InstalledAppFlow.from_client_config(
        client_config,
        SCOPES,
    )

    # access_type="offline" + prompt="consent" ensures we get a refresh token
    creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")

    print("\n=== COPY THIS INTO YOUR .env AS GOOGLE_REFRESH_TOKEN ===\n")
    print(creds.refresh_token)
    print("\n========================================================\n")

if __name__ == "__main__":
    main()
