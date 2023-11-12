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
    scopes = ["https://www.googleapis.com/auth/calendar.readonly"]
    creds_file = 'credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        creds_file,
        scopes = scopes
    )

    service = build(
        'calendar',
        'v3',
        credentials = creds
    ) 

    return service


def get_events(calendar_service):
    est = pytz.timezone('America/New_York')
    now = datetime.datetime.now(est)
    start_of_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=est)
    end_of_day = datetime.datetime(now.year, now.month, now.day, 23, 59, 59, tzinfo=est)

    events_result = calendar_service.events().list(
        calendarId = 'mnovicio2001@gmail.com',
        timeMin= start_of_day.isoformat(),
        timeMax= end_of_day.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get(
        'items',
        []
    )

    return events

# def get_today_events(calendar_service):
#     try:
#         est = pytz.timezone('America/New_York')
#         now = datetime.datetime.now(est)
#         start_of_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=est)
#         end_of_day = datetime.datetime(now.year, now.month, now.day, 23, 59, 59, tzinfo=est)

#         events_result = calendar_service.events().list(
#             calendarId= 'mnovicio2001@gmail.com',
#             timeMin=start_of_day.isoformat(),
#             timeMax=end_of_day.isoformat(),
#             singleEvents=True,
#             orderBy='startTime'
#         ).execute()

#         events = events_result.get('items', [])
#         if not events:
#             print('No events found for today.')
#         else:
#             print('Events for today:')
#             for event in events:
#                 start = event['start'].get('dateTime', event['start'].get('date'))
#                 print(f"{start}: {event['summary']}")

#     except Exception as e:
#         print(f"An error occurred: {e}")


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
        message += f"{start_time} - {end_time}: {event_summary}\n"  # Use += to append


    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=RECIPIENT_PHONE_NUMBER
    )



def main():
   cal_service = get_google_calendar()
   schedule = get_events(cal_service)
   text_schedule(schedule)

if __name__ == '__main__':
    main()


    

    



    