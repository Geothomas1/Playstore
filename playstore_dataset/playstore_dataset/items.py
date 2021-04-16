
import scrapy


class PlaystoreDatasetItem(scrapy.Item):
    # define the fields for your item here like: 
    Link=scrapy.Field()
    Item_name=scrapy.Field()
    Updated=scrapy.Field()
    Author=scrapy.Field()
    Filesize=scrapy.Field()
    Downloads=scrapy.Field()
    Version=scrapy.Field()
    Compatibility=scrapy.Field()
    Content_ratin=scrapy.Field()
    Author_link=scrapy.Field()
    Genre=scrapy.Field()
    Price=scrapy.Field()
    Rating_value=scrapy.Field()
    Review_number=scrapy.Field()
    Description=scrapy.Field()
    IAP=scrapy.Field()
    Developers_bagde=scrapy.Field()
    Physical_address=scrapy.Field()
    Video_URL=scrapy.Field()
    Developers_ID=scrapy.Field()

    pass
