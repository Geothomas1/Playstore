import pprint

from google_play_scraper import permissions

result = permissions(
    'com.carrotpop.www.smth',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
)
pprint.pprint(result)
