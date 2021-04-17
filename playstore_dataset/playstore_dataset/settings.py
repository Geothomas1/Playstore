
BOT_NAME = 'playstore_dataset'

SPIDER_MODULES = ['playstore_dataset.spiders']
NEWSPIDER_MODULE = 'playstore_dataset.spiders'

ROBOTSTXT_OBEY = True

FEED_FORMAT="csv"
FEED_URI="play.csv"
