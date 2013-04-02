# Scrapy settings for fourchan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'fourchan'

SPIDER_MODULES = ['fourchan.spiders']
NEWSPIDER_MODULE = 'fourchan.spiders'

DOWNLOAD_DELAY = 4.5
RANDOMIZE_DOWNLOAD_DELAY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fourchan (+http://www.yourdomain.com)'
