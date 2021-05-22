import scrapy
from ..items import AppDataItem
from google_play_scraper import app
mylist=['nic.goi.aarogyasetu', 'com.nic.mparivahan', 'nic.hp.niv_reporting']
class AppdataSpider(scrapy.Spider):
    name = 'app_data'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps/details?id='+id
        for id in mylist
        ]

    def parse(self, response):
        # apps=AppDataItem()
        # app_name=response.css('.AHFaub span::text').extract()
        # app_developer_name=response.css('.hrTbp.R8zArc::text').extract()
        # rating=response.css('.pf5lIe div::attr(aria-label)').extract()
        # rate=response.css('.AYi5wd.TBRnV span::text').extract()
        # last_update=response.css('div.IQ1z0d span.htlgb::text').extract()
        # version=response.css('.BgcNfc::text').extract()
        # app_rating=response.css()
        # app_link=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract()  
        # app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        result = app('com.nianticlabs.pokemongo',
        lang='en',
        country='us'
        )
        
        
        yield {
            'app_name':app_name,
            'app_developer_name':app_developer_name,
            'rating':rating,
            'rate':rate,
            'last_update':last_update,
            'version':version
        }