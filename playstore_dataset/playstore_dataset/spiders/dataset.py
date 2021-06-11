import scrapy
from ..items import PlaystoreDatasetItem
main_list=[]
class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfZnJlZV9DT01NVU5JQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljJhLKU&gsr=CijSDiUKIwoddG9wc2VsbGluZ19mcmVlX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljIDVBk'
        ]

    def parse(self, response):
        apps=PlaystoreDatasetItem()
        dev_link=[]
        app_name=response.css('.WsMG1c.nnK0zc::text').extract()
        app_developer=response.css('.KoLSrc::text').extract()
        app_link=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract()  
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        #apps['app_name']=app_name
        # apps['app_developer']=app_developer
        # apps['app_link']=app_link
        #apps['app_developer_link']=app_developer_link
        for link in app_link:
            dev_link.append(link.split('=')[-1])
        #print(dev_link)
        for x in dev_link:
            main_list.append(x)
        temp_list = []
        for i in main_list:
            if i not in temp_list:
                temp_list.append(i)
        mylist = temp_list
        #print(temp_list)
        print("List After removing duplicates ", len(mylist))    
        
        print(mylist)
    




   