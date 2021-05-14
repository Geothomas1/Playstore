import scrapy
from scrapy_splash import SplashRequest
main_list=[]

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
        # script = """
        #     function main(splash)
        #         local num_scrolls = 10
        #         local scroll_delay = 2
        #         local scroll_to = splash:jsfunc("window.scrollTo")
        #         local get_body_height = splash:jsfunc(
        #             "function() {return document.body.scrollHeight;}"
        #             )
        #         assert(splash:go(splash.args.url))
        #         splash:wait(splash.args.wait)
        #         for _ = 1, num_scrolls do
        #             scroll_to(0, get_body_height())
        #             splash:wait(scroll_delay)
        #         end
        #         return splash:html()
        #     end        
        #         """
        url='https://play.google.com/store/search?q=social+media+apps&c=apps'
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
        
        #print(main_list)
        yield {'id':mylist}

    
