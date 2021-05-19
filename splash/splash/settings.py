
BOT_NAME = 'splash'
SPIDER_MODULES = ['splash.spiders']
NEWSPIDER_MODULE = 'splash.spiders'
ROBOTSTXT_OBEY = False
SPLASH_URL = 'http://localhost:8050/'
# ROTATING_PROXY_LIST = [
#     '93.170.97.160:8080',
#     '190.211.82.178:999',
#     '202.142.166.194:8080',
#     '190.9.55.12:8080',
#     '167.179.113.45:3128'
# ]
#PROXY_POOL_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,

}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


# SPLASH_URL = 'http://localhost:8050'
# DOWNLOADER_MIDDLEWARES = {
# ...
# 'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
# 'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
# 'scrapy_splash.SplashCookiesMiddleware': 723,
# 'scrapy_splash.SplashMiddleware': 725,
# 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# ...
# }
