import scrapy
from ..items import PlaystoreDatasetItem

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
        'https://play.google.com/store/apps/collection/cluster?clp=6gswCi4KKHByb21vdGlvbl9kYXlkcmVhbV9zdG9yZWNhdGVnb3J5X2FyZ2FtZXMQShgD:S:ANO1ljID8iM&gsr=CjPqCzAKLgoocHJvbW90aW9uX2RheWRyZWFtX3N0b3JlY2F0ZWdvcnlfYXJnYW1lcxBKGAM%3D:S:ANO1ljKbARQ'
        ]

    def parse(self, response):
        apps=PlaystoreDatasetItem()
        app_name=response.css('.WsMG1c.nnK0zc::text').extract()
        app_developer=response.css('.KoLSrc::text').extract()
        app_link=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract()  
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        #apps['app_name']=app_name
        # apps['app_developer']=app_developer
        # apps['app_link']=app_link
        #apps['app_developer_link']=app_developer_link
        for link in app_developer_link:
            print(link.split('=')[-1])

        yield apps


   