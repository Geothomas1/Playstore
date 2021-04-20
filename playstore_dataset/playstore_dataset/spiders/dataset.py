import scrapy
from ..items import PlaystoreDatasetItem
main_list=[]
class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfZnJlZV9BUlRfQU5EX0RFU0lHThAHGAM%3D:S:ANO1ljKKwsU&gsr=CinSDiYKJAoedG9wc2VsbGluZ19mcmVlX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljK_3F0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4iCiAKGnRvcGdyb3NzaW5nX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljIXYIY&gsr=CiXSDiIKIAoadG9wZ3Jvc3NpbmdfQVJUX0FORF9ERVNJR04QBxgD:S:ANO1ljIQjsw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHW1vdmVyc19zaGFrZXJzX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljLIuvY&gsr=CijSDiUKIwodbW92ZXJzX3NoYWtlcnNfQVJUX0FORF9ERVNJR04QBxgD:S:ANO1ljI5X-E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4mCiQKHnRvcHNlbGxpbmdfcGFpZF9BUlRfQU5EX0RFU0lHThAHGAM%3D:S:ANO1ljLn4cw&gsr=CinSDiYKJAoedG9wc2VsbGluZ19wYWlkX0FSVF9BTkRfREVTSUdOEAcYAw%3D%3D:S:ANO1ljK90S4',
        'https://play.google.com/store/apps/collection/cluster?clp=6gsoCiYKIHByb21vdGlvbl9hcl9zdG9yZWNhdGVnb3J5X2FyZWR1EEoYAw%3D%3D:S:ANO1ljLVBCs&gsr=CivqCygKJgogcHJvbW90aW9uX2FyX3N0b3JlY2F0ZWdvcnlfYXJlZHUQShgD:S:ANO1ljIwMKs',
        'https://play.google.com/store/apps/collection/cluster?clp=6gstCisKJXByb21vdGlvbl9kYXlkcmVhbV9hcl9jb3ZpZF9lZHVjYXRpb24QShgD:S:ANO1ljIr61g&gsr=CjDqCy0KKwolcHJvbW90aW9uX2RheWRyZWFtX2FyX2NvdmlkX2VkdWNhdGlvbhBKGAM%3D:S:ANO1ljJnKTg',
        'https://play.google.com/store/apps/collection/cluster?clp=6gsxCi8KKXByb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2Jlc3RvZmFyEEoYAw%3D%3D:S:ANO1ljI3sew&gsr=CjTqCzEKLwopcHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYmVzdG9mYXIQShgD:S:ANO1ljJFdTc',
        'https://play.google.com/store/apps/collection/cluster?clp=6gsvCi0KJ3Byb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2FyYXBwcxBKGAM%3D:S:ANO1ljLDFOc&gsr=CjLqCy8KLQoncHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYXJhcHBzEEoYAw%3D%3D:S:ANO1ljKjMrE',
        'https://play.google.com/store/apps/collection/cluster?clp=6gswCi4KKHByb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2FyZ2FtZXMQShgD:S:ANO1ljID8iM&gsr=CjPqCzAKLgoocHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYXJnYW1lcxBKGAM%3D:S:ANO1ljKbARQ',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIXRvcHNlbGxpbmdfZnJlZV9BVVRPX0FORF9WRUhJQ0xFUxAHGAM%3D:S:ANO1ljL6W3A&gsr=CizSDikKJwohdG9wc2VsbGluZ19mcmVlX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljI4VxE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcGdyb3NzaW5nX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljKFzY4&gsr=CijSDiUKIwoddG9wZ3Jvc3NpbmdfQVVUT19BTkRfVkVISUNMRVMQBxgD:S:ANO1ljLTBqo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4oCiYKIG1vdmVyc19zaGFrZXJzX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljJrBjA&gsr=CivSDigKJgogbW92ZXJzX3NoYWtlcnNfQVVUT19BTkRfVkVISUNMRVMQBxgD:S:ANO1ljK4yRw',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4pCicKIXRvcHNlbGxpbmdfcGFpZF9BVVRPX0FORF9WRUhJQ0xFUxAHGAM%3D:S:ANO1ljI75E8&gsr=CizSDikKJwohdG9wc2VsbGluZ19wYWlkX0FVVE9fQU5EX1ZFSElDTEVTEAcYAw%3D%3D:S:ANO1ljJyZ6w',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9CRUFVVFkQBxgD:S:ANO1ljLNjvk&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0JFQVVUWRAHGAM%3D:S:ANO1ljIGC5s',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4aChgKEnRvcGdyb3NzaW5nX0JFQVVUWRAHGAM%3D:S:ANO1ljLcvug&gsr=Ch3SDhoKGAoSdG9wZ3Jvc3NpbmdfQkVBVVRZEAcYAw%3D%3D:S:ANO1ljKI1x8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFW1vdmVyc19zaGFrZXJzX0JFQVVUWRAHGAM%3D:S:ANO1ljI3S4E&gsr=CiDSDh0KGwoVbW92ZXJzX3NoYWtlcnNfQkVBVVRZEAcYAw%3D%3D:S:ANO1ljKfIuU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9CRUFVVFkQBxgD:S:ANO1ljIF2qM&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0JFQVVUWRAHGAM%3D:S:ANO1ljIZfJ0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4rCikKI3RvcHNlbGxpbmdfZnJlZV9CT09LU19BTkRfUkVGRVJFTkNFEAcYAw%3D%3D:S:ANO1ljJ2D4g&gsr=Ci7SDisKKQojdG9wc2VsbGluZ19mcmVlX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljIiZrU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4nCiUKH3RvcGdyb3NzaW5nX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljL_ufs&gsr=CirSDicKJQofdG9wZ3Jvc3NpbmdfQk9PS1NfQU5EX1JFRkVSRU5DRRAHGAM%3D:S:ANO1ljJw454',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4qCigKIm1vdmVyc19zaGFrZXJzX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljL_ZcY&gsr=Ci3SDioKKAoibW92ZXJzX3NoYWtlcnNfQk9PS1NfQU5EX1JFRkVSRU5DRRAHGAM%3D:S:ANO1ljI0OG0',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4rCikKI3RvcHNlbGxpbmdfcGFpZF9CT09LU19BTkRfUkVGRVJFTkNFEAcYAw%3D%3D:S:ANO1ljLRUDc&gsr=Ci7SDisKKQojdG9wc2VsbGluZ19wYWlkX0JPT0tTX0FORF9SRUZFUkVOQ0UQBxgD:S:ANO1ljIa7_Y',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfZnJlZV9CVVNJTkVTUxAHGAM%3D:S:ANO1ljLX_9I&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19mcmVlX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljIQk5E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcGdyb3NzaW5nX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljKjFx8&gsr=Ch_SDhwKGgoUdG9wZ3Jvc3NpbmdfQlVTSU5FU1MQBxgD:S:ANO1ljI1NO8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4fCh0KF21vdmVyc19zaGFrZXJzX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljKNUP4&gsr=CiLSDh8KHQoXbW92ZXJzX3NoYWtlcnNfQlVTSU5FU1MQBxgD:S:ANO1ljICTN4',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfcGFpZF9CVVNJTkVTUxAHGAM%3D:S:ANO1ljILu9E&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19wYWlkX0JVU0lORVNTEAcYAw%3D%3D:S:ANO1ljL4cI8',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9DT01JQ1MQBxgD:S:ANO1ljITZ68&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0NPTUlDUxAHGAM%3D:S:ANO1ljKZ2sc',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4aChgKEnRvcGdyb3NzaW5nX0NPTUlDUxAHGAM%3D:S:ANO1ljLTs7k&gsr=Ch3SDhoKGAoSdG9wZ3Jvc3NpbmdfQ09NSUNTEAcYAw%3D%3D:S:ANO1ljIooKo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4dChsKFW1vdmVyc19zaGFrZXJzX0NPTUlDUxAHGAM%3D:S:ANO1ljLvqPo&gsr=CiDSDh0KGwoVbW92ZXJzX3NoYWtlcnNfQ09NSUNTEAcYAw%3D%3D:S:ANO1ljLcI_E',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfcGFpZF9DT01JQ1MQBxgD:S:ANO1ljJmiCw&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19wYWlkX0NPTUlDUxAHGAM%3D:S:ANO1ljILjYE',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfZnJlZV9DT01NVU5JQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljJhLKU&gsr=CijSDiUKIwoddG9wc2VsbGluZ19mcmVlX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljIDVBk',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4hCh8KGXRvcGdyb3NzaW5nX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljJi3A0&gsr=CiTSDiEKHwoZdG9wZ3Jvc3NpbmdfQ09NTVVOSUNBVElPThAHGAM%3D:S:ANO1ljJ7Efo',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4kCiIKHG1vdmVyc19zaGFrZXJzX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljKs21c&gsr=CifSDiQKIgocbW92ZXJzX3NoYWtlcnNfQ09NTVVOSUNBVElPThAHGAM%3D:S:ANO1ljJUGKU',
        'https://play.google.com/store/apps/collection/cluster?clp=0g4lCiMKHXRvcHNlbGxpbmdfcGFpZF9DT01NVU5JQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljLE4oc&gsr=CijSDiUKIwoddG9wc2VsbGluZ19wYWlkX0NPTU1VTklDQVRJT04QBxgD:S:ANO1ljI8da0'



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
        print(dev_link)
        for x in dev_link:
            main_list.append(x)
        print(main_list)
        yield apps




   