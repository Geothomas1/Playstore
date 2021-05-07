import scrapy
from ..items import KeywordsItem
main_list=[]
tags=[
'Activity tracker',
'Air Travel',
'Art & design',
'Audio recorder',
'Audiobook',
'Auto & vehicles',
'Baby care',
'Barcode scanner',
'Baseball',
'Beauty',
'Boating',
'Books & reference',
'Bus',
'Business',
'Communication',
'Early childhood education',
'Education',
'Email',
'Emoji',
'Encyclopedia',
'Entertainment',
'Events',
'Fashion',
'Finance',
'Flashlight',
'Food & drink',
'Food delivery',
'Health & Fitness',
'Lifestyle',
'Music & audio',
'Network connectivity',
'Parenting',
'Personalisation',
'Professional network service',
'Pronunciation',
'Public transport',
'Racing',
'Racquet sports',
'Radio',
'Recipe',
'Religious text',
'Remote control',
'Restaurant',
'Resume',
'Ringtone',
'Rugby',
'Running',
'Science education',
'Self-help',
'Shopping',
'Skiing',
'Sleep',
'Social',
'Sound effect',
'Speedometer',
'Sports',
'Sports coaching',
'Study guide',
'Taxi rideshare',
'Tennis',
'Test preparation',
'Text messaging',
'Theme',
'Tools',
'Train',
'Travel & local',
'Travel guide',
'TV',
'TV guide',
'Vehicle maintenance',
'Vehicle shopping',
'Video call',
'Video download',
'Video editing',
'Video player',
'Video streaming',
'Virtual private network',
'Virtual reality',
'Wallpaper',
'Weather',
'Web browser',
'Weight loss',
'Wi-fi',
'Wireless service provider',
'Workout',
'Yoga',
]
class DatasetSpider(scrapy.Spider):
    name = 'keywords'
    allowed_domains=["play.google.com"]
    start_urls=[
            'https://play.google.com/store/search?q='+tag+'&c=apps'
            for tag in tags
            ]
    def parse(self, response):
        apps=KeywordsItem()
        dev_link=[]
        # for item in selector.css('div.')
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        for link in app_developer_link:
            dev_link.append(link.split('=')[-1])
        for x in dev_link:
            main_list.append(x)
        #print(main_list)    
        print(len(main_list))
        #print(main_list)
        yield {'id':main_list}
        




   