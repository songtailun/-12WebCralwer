# -*- coding: utf-8 -*-
from scrapy import signals  
import json  
import codecs
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdcrawlerPipeline(object):
    
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb',
			host = 'localhost',
			port = 3306,
			db = '234',
			user = 'root',
			passwd = '',
			cursorclass = MySQLdb.cursors.DictCursor,
			charset = 'utf8',
			use_unicode = True
			)
			
	def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		return item

	def _conditional_insert(self, tx, item):
		tx.execute("insert into reviews values ('%s')"% MySQLdb.escape_string(item['review'].decode('gb2312').encode('utf8')))