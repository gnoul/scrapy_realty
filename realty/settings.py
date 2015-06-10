# -*- coding: utf-8 -*-

# Scrapy settings for realty project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'realty'

SPIDER_MODULES = ['realty.spiders']
NEWSPIDER_MODULE = 'realty.spiders'


DEFAULT_ITEM_CLASS = 'realty.items.RealtyItem'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'realty (+http://www.yourdomain.com)'
