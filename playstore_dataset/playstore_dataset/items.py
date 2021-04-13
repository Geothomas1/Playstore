
import scrapy


class PlaystoreDatasetItem(scrapy.Item):
    # define the fields for your item here like:
    app_name = scrapy.Field()
    app_developer = scrapy.Field()

    pass
