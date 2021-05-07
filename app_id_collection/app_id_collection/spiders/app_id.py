import scrapy
from ..items import AppIdCollectionItem
mylist=["YovoGames", "Beansprites+LLC", "YovoGames", "8983550861078733583", "5735447750101420287", "5735447750101420287", "Breet.Jia", "9169504509079500539", "8983550861078733583", "bmapps", "kukipukie", "bmapps", "Crazyplex+LLC", "4946022439885210717", "bmapps", "5030558259263481203", "bmapps", "4946022439885210717", "Burbuja+Games", "7518640404124942658", "Beansprites+LLC", "bmapps", "Taprix", "Happy+Apps+Media", "5030558259263481203", "4700756200397995264", "Coco+Play+By+TabTale", "Girls+Games+Studios", "HAPPY+TAPPY+STUDIO", "kids+GamesOn", "5735447750101420287", "GameiFun+-+Educational+games", "6799243928407092181", "gkgame", "5641067919817566915", "5735447750101420287", "Tap+Happy", "PRT+Game+Studio", "9154300028955433686", "4946022439885210717", "Fabulous+Fun", "Mobi+Fun+games", "Fabulous+Fun", "5030558259263481203", "bweb+media", "7082178223243563741", "Chic+World", "Girls+Fashion+Entertainment", "Girl+Games+Academy", "6493980387780624296"]

#sample id data as list
main_list=[]
class AppidSpider(scrapy.Spider):
    name='app_id'
    allowed_domain=["play.google.com"]
    
    start_urls=[
            "https://play.google.com/store/apps/dev?id="+i
            for i in mylist
            ]

    def parse(self,response):
        apps=AppIdCollectionItem()
        app_id_list=[]
        app_id=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract() 

        for link in app_id:
            app_id_list.append(link.split('=')[-1])
        for x in app_id_list:
            main_list.append(x)
        print(main_list)
        print(len(main_list))
        more=response.css('div.W9yFB a::attr(href)').get()
        print(more)
        if more is not None:
            more=response.urljoin(more)
        yield scrapy.Request(more,callback=self.parse)



