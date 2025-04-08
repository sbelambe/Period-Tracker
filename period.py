import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def authenticate_google_account():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("calendar", "v3", credentials=creds)

def add_events(service):
    # Example array of events with start and end dates
    events = [
        {"summary": "Period", "start": "2025-04-10T09:00:00Z", "end": "2025-04-15T10:00:00Z"}
        # {"summary": "Period End", "start": "2025-04-15T09:00:00Z", "end": "2025-04-15T10:00:00Z"},
        # {"summary": "Period Start", "start": "2025-05-10T09:00:00Z", "end": "2025-05-10T10:00:00Z"},
        # {"summary": "Period End", "start": "2025-05-15T09:00:00Z", "end": "2025-05-15T10:00:00Z"}
    ]

    for event_data in events:
        event = {
            "summary": event_data["summary"],
            "start": {
                "dateTime": event_data["start"],
                "timeZone": "UTC",
            },
            "end": {
                "dateTime": event_data["end"],
                "timeZone": "UTC",
            },
        }
        try:
            created_event = service.events().insert(
                calendarId="primary", body=event
            ).execute()
            print(f"Event created: {created_event['summary']} on {created_event['start']['dateTime']}")
        except HttpError as error:
            print(f"An error occurred: {error}")

def main():
    try:
        # Authenticate and create the Google Calendar service
        service = authenticate_google_account()

        # Add events to the calendar
        add_events(service)
    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
