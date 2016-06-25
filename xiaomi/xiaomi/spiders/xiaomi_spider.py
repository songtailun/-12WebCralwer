import scrapy
import re  
from scrapy import Spider
from scrapy.selector import Selector
from xiaomi.items import XiaomiItem


class xiaomi_spider(Spider):
    name = "xiaomi"
    allowed_domains = ["http://app.mi.com"]
    start_urls = [
        "http://app.mi.com"
    ]
    '''
    def parse(self, response):
        sel = Selector(response)
        contents = sel.xpath('//div[@class="applist-wrap"]/ul[@class="applist"]/li')
        #items = []


        for content in contents:
        	item = XiaomiItem()
        	item['title'] = content.xpath('h5/a/text()').extract()[0]
        	#item['title'] = len(item['title'])
        	item['url'] = content.xpath('h5/a/@href').extract()[0]
        	yield item
    '''
    def find_next_page(self, url):
        try:
            page_num_str = url.split('=')[-1]
            page_num = int(page_num_str)+1
            #Limit the number of pages crawl for testing
            if page_num > 67:
                return None

            url = url[:-len(page_num_str)] + str(page_num)
            return url
        except ValueError:
            print "### next page url cannot be handled"
            print url
            return None
    def start_requests(self):

        baseurl="http://app.mi.com/category/"
        for k in range(1, 30):
            newurl = baseurl + str(k) + "#page=0"
            self.start_urls.append(newurl)

        for url in self.start_urls:
            while url:
                print 'request: ' + url
                yield scrapy.Request(url, self.parse_page, dont_filter=True, meta={
                            'splash': {
                                'endpoint': "render.html",
                                'args': {'wait': 0.8},
                                'magic_response': True,
                            }
                        })
                url = self.find_next_page(url)
    def parse_page(self, response):
        page = Selector(response)
        #Get the url for every app on the page
        hrefs = page.xpath('//ul[@id="all-applist"]/li/h5/a/@href')

        for href in hrefs:
            url = self.base_url + href.extract()
            yield scrapy.Request(url, callback=self.parse_item)
    def parse_item(self, response):
        page = Selector(response)

        divs = page.xpath('//div[@class="intro-titles"]')
        s = ""
        des = []
        for div in divs:
            item = AppstoreCrawlerItem()
            item['title'] = div.xpath('./h3/text()').extract()[0].encode('utf-8')
            item['url'] = response.url
            item['appid'] = re.match(r'.*/detail/(.*)', item['url']).group(1)
            item['intro'] = div.xpath('./p[2]/text()[1]').extract()[0].encode('utf-8')
            item['company'] = div.xpath('./p[1]/text()').extract_first().encode('utf-8')
            des = page.xpath(
                '//div[@class="app-text"]/p[@class="pslide"][1]/text()').extract()
            for x in des:
                s = s+str(x)
            item['describe'] = s

            yield item

