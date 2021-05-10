import scrapy
from scrapy_splash import SplashRequest
main_list=[]

class DynamicSpider(scrapy.Spider):
    name = 'dynamic'
    allowed_domains = ['x']
    
    def start_requests(self):
        tags=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in tags:
            url='https://play.google.com/store/search?q='+i+'&c=apps'
            yield SplashRequest(url,callback=self.parse)

    def parse(self, response):
        dev_link=[]
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        for link in app_developer_link:
            dev_link.append(link.split('=')[-1])
            for x in dev_link:
                main_list.append(x)
        print(len(main_list))
        temp_list = []
        for i in main_list:
            if i not in temp_list:
                temp_list.append(i)
        mylist = temp_list
        #print(temp_list)
        print("List After removing duplicates ", len(mylist))    
        
        #print(main_list)
        yield {'id':mylist}

    
