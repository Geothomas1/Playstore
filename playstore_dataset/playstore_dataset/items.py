
import scrapy

class PlaystoreDatasetItem(scrapy.Item):
    # define the fields for your item here like:
    app_name = scrapy.Field()
    app_developer = scrapy.Field()
    app_link=scrapy.Field()
    app_developer_link=scrapy.Field()
    link=scrapy.Field()

    pass

