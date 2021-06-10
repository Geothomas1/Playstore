from google_play_scraper import permissions
import urllib
import google_play_scraper
import requests
from google_play_scraper import app
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pprint

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID a sample spreadsheet.
SPREADSHEET_ID = '1r1ifW642gcbAxDN6NbktgFhxUMhqRCKJx3CK8E82UsA'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

mylist=['bharat.browser']

#Testing for API 

print(len(mylist))
c=0
data = []
for i in mylist:
    try:
        result = permissions(i,lang='en',country='us')
        data.append([
        i,
        len(result['Camera']) if 'Camera' in result.keys() else 0,
        len(result['Contacts']) if 'Contacts' in result.keys() else 0 ,
        len(result['Device & app history']) if 'Device & app history' in result.keys() else  0,
        len(result['Device ID & call information']) if 'Device & app history' in result.keys() else 0 ,
        len(result['Identity'])  if 'Identity' in result.keys() else 0,
        len(result['Location']) if 'Location' in result.keys() else  0,
        len(result['Microphone']) if 'Microphone' in result.keys() else 0,
        len(result['Phone']) if 'Phone' in result.keys() else 0,
        len(result['Photos/Media/Files']) if 'Photos/Media/Files' in result.keys() else 0,
        len(result['SMS'])  if 'SMS' in result.keys() else  0,
        len(result['Storage']) if 'Storage' in result.keys() else 0,
        len(result['Uncategorized']) if 'Uncategorized' in result.keys() else 0,
        len(result['Wi-Fi connection information'])  if 'Wi-Fi connection information' in result.keys() else 0,
        len(result['Calendar'])if 'Calendar' in result.keys() else  0,
        len(result['Other']) if 'Other' in result.keys() else 0
        ])
        print(c)
        print(mylist[c])
        c=c+1
    
    except urllib.error.HTTPError:
        print('Urllib Error HttpError Skip 1')
        continue
    except google_play_scraper.exceptions.NotFoundError:
        print('google play scraper exception Skip 2')
        continue
    except AttributeError:
        print("Attribute Error Exception Skip 3")
        continue
    except ValueError:
        print('Value Exception Skip 3')
        continue
    except requests.exceptions.HTTPError:
        print('Request Exception Skip 4')
        continue
    except google_play_scraper.exceptions.ExtraHTTPError:
        print("google_play_scraper.exceptions.ExtraHTTPError Skip 5")
        continue   
print(data)
# for i in range(len(data[0])):
#     for j in range(len(data[0][i])):
#         pprint.pprint(data[0][i][j])
result1 = sheet.values().append(spreadsheetId=SPREADSHEET_ID,range="Sheet3!A1:P1", valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS",body={"values":data}).execute()