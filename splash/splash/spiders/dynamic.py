import scrapy
from scrapy_splash import SplashRequest
main_list=[]
key=[
    'photo+editor'
]
class DynamicSpider(scrapy.Spider):
    name = 'dynamic'
    allowed_domains = ['x']
    def start_requests(self):
        script = """
                    function main(splash,args)
                        splash:set_viewport_size(1028, 10000)
                        splash:go(args.url)
                        local scroll_to = splash:jsfunc("window.scrollTo")
                        scroll_to(0, 2900)
                        splash:wait(8)
                        return {
                            html = splash:html()
                        }
                    end
                  """    
        for i in key:
            url='https://play.google.com/store/search?q='+i+'&c=apps'
            yield SplashRequest(url, self.parse,  endpoint='execute', args={'lua_source': script, 'url': url})

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
        
        print(mylist)

    
