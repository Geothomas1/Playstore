import scrapy
from ..items import KeywordsItem
main_list=[]
tags=['4X',
'Abstract strategy',
'Action',
'Action role-playing',
'Action-adventure',
'Adventure',
'American football',
'Arcade',
'Basketball',
'Beat ‘em up',
'Billiards',
'Bingo',
'Blackjack',
'Board',
'Bowling',
'Boxing',
'Brain training',
'Brick break',
'Bubble shooter',
'Business & tycoon',
'Car racing',
'Car simulator',
'Card',
'Care simulation',
'Casino',
'Casual',
'Checkers',
'Chess',
'City-building',
'Collectible cards',
'Construction and management simulation',
'Cricket',
'Crossword',
'Dating simulation',
'Dentist',
'Dice',
'Doctor',
'Drawing',
'Dress-up',
'Drums',
'Educational',
'Endless runner',
'Escape the room',
'Farming',
'Fighting',
'Flight simulator',
'Go',
'Golf',
'Government & political',
'Hero shooter',
'Hidden object',
'Hockey',
'Incremental',
'Interactive fiction',
'Japanese role-playing',
'Jigsaw puzzle',
'Kart racing',
'Life simulation',
'Logo quiz',
'Ludo',
'Mahjong',
'Mahjong solitaire',
'Massively multiplayer online role-playing',
'Match 3',
'Memory',
'Merge puzzle',
'Motorcycle racing',
'Multiplayer online battle arena',
'Music',
'Pet',
'Physics-based',
'Piano',
'Platform action-adventure',
'Platformer',
'Poker',
'Puzzle',
'Puzzle role-playing',
'Puzzle-adventure',
'Racing',
'Racing simulator',
'Restaurant & cooking',
'Rhythm',
'Roguelike',
'Role-playing',
'Rummy',
'Shoot ‘em up',
'Shooter',
'Shooting range',
'Simulation',
'Sliding puzzle',
'Slot machine',
'Soccer',
'Social simulation',
'Solitaire',
'Sports',
'Sports management',
'Sports-based fighting',
'Strategy',
'Stunt driving',
'Survival',
'Survival horror',
'Table game',
'Tactical role-playing',
'Teen patti',
'Tile-matching',
'Tower defense',
'Train simulator',
'Trivia',
'Truck racing',
'Truck simulator',
'Vehicle simulation',
'Visual novel',
'Wargame',
'Winter sports',
'Word',
'Word search',
'Wrestling',
]
class DatasetSpider(scrapy.Spider):
    name = 'keywords'
    allowed_domains=["play.google.com"]
    start_urls = [
        'https://play.google.com/store/search?q='+tag+'&c=apps'
        for tag in tags
        ]

    def parse(self, response):
        apps=KeywordsItem()
        dev_link=[]
        # for item in selector.css('div.')
        app_developer_link=response.css('.b8cIId.ReQCgd.KoLSrc a.mnKHRc::attr(href)').extract()
        for link in app_developer_link:
            dev_link.append(link.split('=')[-1])
        for x in dev_link:
            main_list.append(x)
        #print(main_list)    
        print(len(main_list))
        yield {'l':apps}
        




   