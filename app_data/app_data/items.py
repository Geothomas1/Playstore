# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AppDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_name=scrapy.Field()
    app_developer_name=scrapy.Field()
    rating=scrapy.Field()
    rate=scrapy.Field()
    last_update=scrapy.Field()
    version=scrapy.Field()
    pass
