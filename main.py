from google.oauth2 import service_account 
from googleapiclient.discovery import build 
import pytz 

def main():
    print('the supported timezones by the pytz module:',
      pytz.all_timezones, '\n')

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

print('the supported timezones by the pytz module:',
      pytz.all_timezones, '\n')

def get_events():
    est = pytz.timezone('America/New York')
    now = datetime.now(est)












    