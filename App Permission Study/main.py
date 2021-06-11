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
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID a sample spreadsheet.
SPREADSHEET_ID = '1r1ifW642gcbAxDN6NbktgFhxUMhqRCKJx3CK8E82UsA'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

mylist = ['com.whatsapp', 'com.truecaller', 'com.whatsapp.w4b', 'org.telegram.messenger', 'com.facebook.orca', 'share.sharekaro.pro', 'com.abtalk.freecall', 'bharat.browser', 'com.bingo.livetalk', 'com.imo.android.imoim', 'com.google.android.apps.messaging', 'com.discord', 'com.opera.mini.native', 'il.co.smedia.callrecorder.yoni', 'com.facebook.mlite', 'com.scarzstudio.scarz', 'com.google.android.contacts', 'x.free.unlimited.global.call', 'com.dartushinc.callername', 'com.callapp.contacts', 'com.mobile.number.locator.phone.gps.map', 'lv.indycall.client', 'com.opera.browser', 'com.ovbdigital.ppubgstickers', 'pro.whatscan.whatsweb.app', 'com.jio.join', 'com.azarlive.android', 'com.eyecon.global', 'uc.ucmini.browser.ucbrowser', 'com.drilens.wamr', 'wastickerapps.stickersforwhatsapp', 'u.browser.for.lite.uc.browser', 'com.touchtalent.bobbleapp', 'com.google.android.apps.tachyon', 'com.uc_browser', 'com.hiiu.live', 'org.mozilla.firefox', 'com.zinn.currentmobiletrackerlocation', 'com.jiochat.jiochatapp', 'im.thebot.messenger', 'truecaller.caller.callerid.name.phone.dialer', 'com.helixdev.onesocial', 'com.xbrowser.play', 'org.thoughtcrime.securesms', 'com.speaktranslate.englishalllanguaguestranslator.ivoicetranslation', 'com.brave.browser', 'livemobiletracker.locationtracker.phonelocator.inviteloop', 'com.imo.android.imoimbeta', 'com.skype.raider', 'livemobilelocationtracker.teccreations']

# Testing for API

print(len(mylist))
c = 0
data = []
for j in mylist:
    try:
        result = permissions(j, lang='en', country='us')
        # result['Camera']
        print(result.keys())
        if 'Camera' in result.keys():
            camera=''
            for i in result['Camera']:
                camera=camera+'\n'+i
        else:
            camera='No Access'
        if 'Contacts' in result.keys():
            contacts=''
            for i in result['Contacts']:
                contacts=contacts+'\n'+i
        else:
            contacts='No Access'
        if 'Device & app history' in result.keys():
            deviceApp=''
            for i in result['Device & app history']:
                deviceApp=deviceApp+'\n'+i
        else:
            deviceApp='No Access'
        if 'Device ID & call information' in result.keys():
            deviceCall=''
            for i in result['Device ID & call information']:
                deviceCall=deviceCall+'\n'+i
        else:
            deviceCall='No Access'
        if 'Identity' in result.keys():
            identity=''
            for i in result['Identity']:
                identity=identity+'\n'+i
        else:
            identity='No Access'
        if 'Location' in result.keys():
            location=''
            for i in result['Location']:
                location=location+'\n'+i
        else:
            location='No Access'
        if 'Microphone' in result.keys():
            microphone=''
            for i in result['Microphone']:
                microphone=microphone+'\n'+i
        else:
            microphone='No Access'
        if 'Phone' in result.keys():
            phone=''
            for i in result['Phone']:
                phone=phone+'\n'+i
        else:
            phone='No Access'
        if 'Photos/Media/Files' in result.keys():
            pmf=''
            for i in result['Photos/Media/Files']:
                pmf=pmf+'\n'+i
        else:
            pmf='No Access'
        if 'SMS' in result.keys():
            sms=''
            for i in result['SMS']:
                sms=sms+'\n'+i
        else:
            sms='No Access'
        if 'Storage' in result.keys():
            storage=''
            for i in result['Storage']:
                storage=storage+'\n'+i
        else:
            storage='No Access'
        if 'Uncategorized' in result.keys():
            uncategorized=''
            for i in result['Uncategorized']:
                uncategorized=uncategorized+'\n'+i
        else:
            uncategorized='No Access'
        if 'Wi-Fi connection information' in result.keys():
            wifi=''
            for i in result['Wi-Fi connection information']:
                wifi=wifi+'\n'+i
        else:
            wifi='No Access'
        if 'Calendar' in result.keys():
            calender=''
            for i in result['Calendar']:
                calender=calender+'\n'+i
        else:
            calender='No Access'

        if 'Other' in result.keys():
            other=''
            for i in result['Other']:
                other=other+'\n'+i
        else:
            other='No Access'
        data.append([j,camera,contacts,deviceApp,deviceCall,identity,location,microphone,phone,pmf,sms,storage,uncategorized,wifi,calender,other])
        print(c)
        print(mylist[c])
        c = c+1

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

# for i in range(len(data[0])):
#     for j in range(len(data[0][i])):
#         pprint.pprint(data[0][i][j])
result1 = sheet.values().append(spreadsheetId=SPREADSHEET_ID,range="Sheet3!A1:P1", valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS",body={"values":data}).execute()
