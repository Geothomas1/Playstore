import scrapy
from ..items import PlaystoreDatasetItem
main_list=[]
class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps/collection/cluster?clp=SisKJQofcHJvbW90aW9uXzMwMDIwZThfbG93YXBrX2FwcHNpbhBKGAM6AggB:S:ANO1ljJNOqc&gsr=Ci1KKwolCh9wcm9tb3Rpb25fMzAwMjBlOF9sb3dhcGtfYXBwc2luEEoYAzoCCAE%3D:S:ANO1ljIhlPE',
        'https://play.google.com/store/apps/collection/cluster?clp=SiIKHAoWcHJvbW90aW9uX3VwZGF0ZWRfYXBwcxBKGAM6AggB:S:ANO1ljJZ1aQ&gsr=CiRKIgocChZwcm9tb3Rpb25fdXBkYXRlZF9hcHBzEEoYAzoCCAE%3D:S:ANO1ljKskiA',
        'https://play.google.com/store/apps/collection/cluster?clp=SjEKKwolcHJvbW90aW9uXzMwMDIxMDNfZ292dHNlcnZpY2VzX2FwcHNpbhBKGAM6AggB:S:ANO1ljKg9wc&gsr=CjNKMQorCiVwcm9tb3Rpb25fMzAwMjEwM19nb3Z0c2VydmljZXNfYXBwc2luEEoYAzoCCAE%3D:S:ANO1ljKl0oc'
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
        for link in app_developer_link:
            dev_link.append(link.split('=')[-1])
        #print(dev_link)
        for x in dev_link:
            main_list.append(x)
        yield {'link':main_list}
        print(len(main_list))
    




   