import scrapy
from ..items import PlaystoreDatasetItem
import 



class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    start_urls = ['https://play.google.com/store/apps']

    def parse(self, response):
        apps=PlaystoreDatasetItem()
        app_name=response.css('.WsMG1c.nnK0zc::text').extract()
        app_developer=response.css('.KoLSrc::text').extract()
        apps['app_name']=app_name
        apps['app_developer']=app_developer
        
        
        yield apps
