from google_play_scraper import app

result = app(
    'com.whatsapp',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)
print(result)