import scrapy
from ..items import AppIdCollectionItem
mylist=[]

#sample id data as list
main_list=['5700313618786177705']
class AppidSpider(scrapy.Spider):
    name='app_id'
    allowed_domain=["play.google.com"]
    
    start_urls=[
        "https://play.google.com/store/apps/dev?id=5700313618786177705"
            ]

    def parse(self,response):
        apps=AppIdCollectionItem()
        app_id_list=[]
        app_id=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract() 

        for link in app_id:
            app_id_list.append(link.split('=')[-1])
        for x in app_id_list:
            main_list.append(x)
        #print(main_list)
        
        more=response.css('div.W9yFB a::attr(href)').get()
        #print(more)
        if more is not None:
            more=response.urljoin(more)
        print(len(main_list))
        yield scrapy.Request(more,callback=self.parse)



