# Scrapy settings for gumtree project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gumtree'

ITEM_PIPELINES = {
    'gumtree.pipelines.MongoDBPipeline': 0,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "gumtree"
MONGODB_COLLECTION = "bikes"

SPIDER_MODULES = ['gumtree.spiders']
NEWSPIDER_MODULE = 'gumtree.spiders'
DOWNLOAD_DELAY = 0.2

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gumtree (+http://www.yourdomain.com)'
