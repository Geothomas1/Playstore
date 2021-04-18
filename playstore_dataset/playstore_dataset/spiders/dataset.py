import scrapy


class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = ['https://play.google.com/store/apps']


    def parse(self, response):
        for app in response.css('div.Ktdaqe'):
            yield
            {
                'app_name':app.css('.WsMG1c.nnK0zc::text').extract(),
                'app_developer':app.css('.KoLSrc::text').extract()
            }


   