import scrapy
from ..items import PlaystoreDatasetItem



class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    start_urls = ['https://play.google.com/store/apps/collection/cluster?clp=SjEKKwolcHJvbW90aW9uXzMwMDIxMDNfZ292dHNlcnZpY2VzX2FwcHNpbhBKGAM6AggB:S:ANO1ljKg9wc&gsr=CjNKMQorCiVwcm9tb3Rpb25fMzAwMjEwM19nb3Z0c2VydmljZXNfYXBwc2luEEoYAzoCCAE%3D:S:ANO1ljKl0oc']

    def parse(self, response):
        apps=PlaystoreDatasetItem()
        app_name=response.css('.WsMG1c.nnK0zc::text').extract()
        app_developer=response.css('.KoLSrc::text').extract()
        apps['app_name']=app_name
        apps['app_developer']=app_developer
        
        yield apps
