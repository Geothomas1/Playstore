import scrapy
from ..items import PlaystoreDatasetItem


class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = ['https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfZnJlZV9BUlRfQU5EX0RFU0lHThAHGAM%3D:S:ANO1ljKKwsU&gsr=CinSDiYKJAoedG9wc2VsbGluZ19mcmVlX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljK_3F0']


    def parse(self, response):
        apps=PlaystoreDatasetItem()
        app_name=response.css('.WsMG1c.nnK0zc::text').extract()
        app_developer=response.css('.KoLSrc::text').extract()
        app_link=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract()  
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        #apps['app_name']=app_name
        # apps['app_developer']=app_developer
        # apps['app_link']=app_link
        apps['app_developer_link']=app_developer_link
        for link in app_developer_link:
            print(link.split('=')[-1])

        yield apps


   