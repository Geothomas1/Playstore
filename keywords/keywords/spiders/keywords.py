import scrapy
from ..items import KeywordsItem
main_list=[]
tags=[
'Afrikaans',
'Amharic',
'Arabic',
'Armenian',
'Azerbaijani',
'Basque',
'Belarusian',
'Bengali',
'Bulgarian',
'Burmese',
'Catalan',
'Chinese',
'Croatian',
'Czech',
'Danish',
'Dutch',
'English',
'Estonian',
'Filipino',
'Finnish',
'French',
'Galician',
'Georgian',
'German',
'Greek',
'Hebrew',
'Hindi',
'Hungarian',
'Icelandic',
'Indonesian',
'Italian',
'Japanese',
'Kannada',
'Khmer',
'Korean',
'Kyrgyz',
'Lao',
'Latvian',
'Lithuanian',
'Macedonian',
'Malay',
'Malayalam',
'Marathi',
'Mongolian',
'Nepali',
'Norwegian',
'Persian',
'Polish',
'Portuguese',
'Portuguese',
'Romanian',
'Romansh',
'Russian',
'Serbian',
'Sinhala',
'Slovak',
'Slovenian',
'Spanish',
'Swahili',
'Swedish',
'Tamil',
'Telugu',
'Thai',
'Turkish',
'Ukrainian',
'Vietnamese',
'Zulu',
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
        




   