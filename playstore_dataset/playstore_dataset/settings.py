
BOT_NAME = 'playstore_dataset'

SPIDER_MODULES = ['playstore_dataset.spiders']
NEWSPIDER_MODULE = 'playstore_dataset.spiders'

ROBOTSTXT_OBEY = True
ROTATING_PROXY_LIST = [
    '93.170.97.160:8080',
    '190.211.82.178:999',
    '202.142.166.194:8080',
    '190.9.55.12:8080',
    '167.179.113.45:3128'
]
DOWNLOADER_MIDDLEWARES = {
    # ...
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
    # ...
}
# PROXY_POOL_ENABLED = True
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
# }
# FEED_FORMAT="csv"
# FEED_URI="play.csv"
