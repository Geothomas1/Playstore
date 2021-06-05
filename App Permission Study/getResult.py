import pprint

from google_play_scraper import permissions
net.one97.paytm,com.phonepe.app
result = permissions(
    '',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
)
pprint.pprint(result)
