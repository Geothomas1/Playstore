# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KeywordsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_developer_link=scrapy.Field()
    pass
