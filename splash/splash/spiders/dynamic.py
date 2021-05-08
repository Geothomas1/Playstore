# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
main_list=[]

class DynamicSpider(scrapy.Spider):
    name = 'dynamic'
    allowed_domains = ['x']
    
    def start_requests(self):
        tags=['Afrikaans'
        ]
        for i in tags:
            url='https://play.google.com/store/search?q='+i+'&c=apps'
            yield SplashRequest(url)

    def parse(self, response):
        apps=response.css('.ImZGtf.mpg5gc')
        for link in apps:
            dev_link=[]
            app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
            for link in app_developer_link:
                dev_link.append(link.split('=')[-1])
                for x in dev_link:
                    main_list.append(x)    
        print(len(main_list))
        #print(main_list)
        yield {'id':main_list}

    
