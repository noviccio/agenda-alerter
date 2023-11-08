from google.oauth2 import service_account 
from googleapiclient.discovery import build 
import pytz 
import datetime
from twilio.rest import Client
import os 
from dotenv import load_dotenv


load_dotenv()
#environment variables 
SID = os.getenv("SID") 
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


def get_google_calendar():
    scopes = ["https://www.googleapis.com/auth/cloud-platform.read-only"]
    creds_file = "credentials.json"

    creds = service_account.Credentials.from_service_account(
        creds_file,
        scopes
    )

    service = build(
        'calendar',
        'v3',
        credentials = creds
    ) 

    return service


def get_events(calendar_service):
    est = pytz.timezone('America/New York')
    now = datetime.now(est)
    end_of_day = datetime(now.year, now.month, now.day, 23, 0, 0)

    events_result = calendar_service.events().list(
        calendarId = 'primary',
        timeMin=now.isoformat(),
        timeMax=end_of_day.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get(
        'items',
        []
    )

    return events

def text_schedule(schedule):
    TWILIO_SID = SID
    TWILIO_AUTH_TOKEN = AUTH_TOKEN
    TWILIO_PHONE_NUMBER = TWILIO_NUMBER
    RECIPIENT_PHONE_NUMBER = PHONE_NUMBER

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    if not schedule:
        message = "You have no events scheduled for today."
    else:
        message = "Your schedule for today:\n"
        for event in schedule: 
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            end_time = event['end'].get('dateTime', event['end'].get('date'))
            event_summary = event['summary']
            message = f"{start_time} - {end_time}: {event_summary}\n"

            message = client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=RECIPIENT_PHONE_NUMBER
            )


def main():
   cal_service = get_google_calendar()
   schedule = get_events(cal_service)
   text_schedule(schedule)





    