# -*- coding: GBK -*-

# Scrapy settings for JDCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'JDCrawler'

SPIDER_MODULES = ['JDCrawler.spiders']
NEWSPIDER_MODULE = 'JDCrawler.spiders'
ITEM_PIPELINES = ['JDCrawler.pipelines.JdcrawlerPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JDCrawler (+http://www.yourdomain.com)'
