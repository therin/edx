# Scrapy settings for horrible project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'horrible'

SPIDER_MODULES = ['horrible.spiders']
NEWSPIDER_MODULE = 'horrible.spiders'
#ITEM_PIPELINES = ['horrible.pipelines.TorrentPipeline']

# Download and traffic settings.
# Limit concurrent requests and add a 
# download delay to minimize hammering.
USER_AGENT = 'http://www.nyaa.eu'
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = False
CONCURRENT_REQUESTS_PER_DOMAIN = 1 #  Default: 8
#SCHEDULER = 'scrapy.core.scheduler.Scheduler'

# Log Settings
#LOG_ENABLED = True
#LOG_LEVEL = 'INFO' # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
#LOG_FILE = './horrible.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'horrible (+http://www.yourdomain.com)'
