import scrapy


class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    start_urls = ['http://https://play.google.com/store/']

    def parse(self, response):
        pass
