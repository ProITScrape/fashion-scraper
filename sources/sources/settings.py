# Scrapy settings for sources project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from shutil import which
import pkgutil


SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
BOT_NAME = 'sources'

SPIDER_MODULES = ['sources.spiders']
NEWSPIDER_MODULE = 'sources.spiders'

RETRY_TIMES = 50
RETRY_HTTP_CODES = [429,403,502,500]
FEED_EXPORT_FIELDS = ["id_product","page_url","adult_kid","gender","category","subcategory1","subcategory2","price","measuring_unit","person_height",
"cloth_size_in_image","cloth_length_in_image","number_of_images_on_page","meta","image_names"]
#CLOSESPIDER_ERRORCOUNT = 1


#ROTATING_PROXY_LIST = ['5.79.73.131:13150']
ROTATING_PROXY_LIST = ['63.141.241.98:16001'
'173.208.209.42:16001'
'69.197.179.122:16001'
'173.208.199.74:16001'
'163.172.36.211:16001'
'163.172.61.67:16001'
'51.15.0.181:16001'
'163.172.214.117:16001']
ROTATING_PROXY_PAGE_RETRY_TIMES=30    
    


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sources (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 50
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'sources.middlewares.SourcesSpiderMiddleware': 543,
    
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'sources.middlewares.SourcesDownloaderMiddleware': 543,
   'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    "sources.middlewares.SleepRetryMiddleware":100,
    #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    #'scrapy_selenium.SeleniumMiddleware': 800
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'sources.pipelines.SourcesPipeline': 300,
    'sources.pipelines.CustomImageNamePipeline':1
}
#LOG_LEVEL = 'ERROR' # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
#LOG_FILE = 'log.log'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
