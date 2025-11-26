# # from __future__ import print_function
# # import os.path

# # from google.auth.transport.requests import Request
# # from google.oauth2.credentials import Credentials
# # from google_auth_oauthlib.flow import InstalledAppFlow

# # SCOPES = [
# #     "https://www.googleapis.com/auth/calendar.events",
# #     "https://www.googleapis.com/auth/gmail.send",
# # ]

# # TOKEN_FILE = "calendar_token.json"
# # CREDS_FILE = "calendar_credentials.json"

# # def main():
# #     creds = None
# #     if os.path.exists(TOKEN_FILE):
# #         creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

# #     if not creds or not creds.valid:
# #         if creds and creds.expired and creds.refresh_token:
# #             creds.refresh(Request())
# #         else:
# #             flow = InstalledAppFlow.from_client_secrets_file(
# #                 CREDS_FILE, SCOPES
# #             )
# #             creds = flow.run_local_server(port=0)

# #         with open(TOKEN_FILE, "w") as token:
# #             token.write(creds.to_json())

# #     print("calendar_token.json created/updated.")

# # if __name__ == "__main__":
# #     main()

# from __future__ import print_function
# import os
# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from dotenv import load_dotenv

# load_dotenv()

# SCOPES = [
#     "https://www.googleapis.com/auth/calendar.events",
#     "https://www.googleapis.com/auth/gmail.send",
# ]

# TOKEN_FILE = "calendar_token.json"

# def main():
#     client_id = os.getenv("GOOGLE_CLIENT_ID")
#     client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

#     if not client_id or not client_secret:
#         raise RuntimeError("GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET is not set in .env")

#     # This replaces the calendar_credentials.json file
#     client_config = {
#         "installed": {
#             "client_id": client_id,
#             "client_secret": client_secret,
#             "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#             "token_uri": "https://oauth2.googleapis.com/token",
#         }
#     }

#     creds = None
#     if os.path.exists(TOKEN_FILE):
#         creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
#             creds = flow.run_local_server(port=0)

#         with open(TOKEN_FILE, "w") as token:
#             token.write(creds.to_json())

#     print("calendar_token.json created/updated.")

# if __name__ == "__main__":
#     main()

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
