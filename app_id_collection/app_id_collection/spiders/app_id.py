import scrapy
from ..items import AppIdCollectionItem

main_list=[]
class AppidSpider(scrapy.Spider):
    name='app_id'
    allowed_domain=["play.google.com"]
    mylist=['9076108670215860604','5700313618786177705']
    start_urls=[
            'https://play.google.com/store/apps/dev?id='+i
            for i in mylist
            ]

    def parse(self,response):
        apps=AppIdCollectionItem()
        app_id_list=[]
        app_id=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract() 
        for link in app_id:
            app_id_list.append(link.split('=')[-1])
        for x in app_id_list:
            main_list.append(x)
        yield {'app_id':main_list}



