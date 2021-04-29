import scrapy
from ..items import KeywordsItem
main_list=[]

class DatasetSpider(scrapy.Spider):
    name = 'keywords'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/search?q&c=apps'
        ]

    def parse(self, response):
        apps=KeywordsItem()
        dev_link=[]
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        for link in app_developer_link:
            dev_link.append(link.split('=')[-1])
        for x in dev_link:
            main_list.append(x)
        yield {'link':main_list}
        print(len(main_list))




   