import pprint

from google_play_scraper import permissions

result = permissions(
    'org.telegram.messenger',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
)
pprint.pprint(result)
