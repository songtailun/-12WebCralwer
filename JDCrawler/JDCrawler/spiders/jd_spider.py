from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector

from JDCrawler.items import JdcrawlerItem

class JDSpider(BaseSpider):
	name = "jd"
	allowed_domains = ["data.auto.sina.com.cn"]
	start_urls = [
		"http://data.auto.sina.com.cn/car_comment/list_406_0.html"
	]
    def parse(self, response):
        items = []
        comments = response.xpath('//dd[@class="j"]/p[@class="zs"]/text()').extract()
        for comment in comments:
            item = JdcrawlerItem()
            #review = comment.xpath('/text()').extract()
            item['review'] = "".join(comment)
            items.append(item)
        return items