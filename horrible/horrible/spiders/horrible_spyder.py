from scrapy.spider import BaseSpider  
from scrapy.selector import HtmlXPathSelector  
from scrapy.http import Request  
from scrapy.utils.response import get_base_url  
from scrapy.contrib.loader import XPathItemLoader
from items import TorrentItem  
  
class horribleSpider(BaseSpider):  
  
 name = "horrible"  
 allowed_domains = ["http://www.nyaa.eu"]
 start_urls = ['http://www.nyaa.eu/?page=search&cats=0_0&filter=0&term=hunter']    
 def parse(self, response):
    hxs = HtmlXPathSelector(response)
    entries = hxs.select('//tr[contains(@class,"trusted tlistrow")]/td[contains(@class, "tlistname")]')
    for entry in entries:
    	l = XPathItemLoader(item=TorrentItem(), selector=entry )
        l.add_xpath('torrent', 'a/@href')
        l.add_xpath('title', 'a[contains(@href, "nyaa")]/text()')
        yield l.load_item() 





'''
 name = "horrible"  
 allowed_domains = ["http://www.nyaa.eu"]
 start_urls = ['http://www.nyaa.eu/?page=search&cats=0_0&filter=0&term=hunter']    
 def parse(self, response):
    hxs = HtmlXPathSelector(response)
    entries = hxs.select('//tr[contains(@class,"tlistrow")]')
    results = []
    for entries in entries:
        result = TorrentItem()  
      	#result['title'] = entry.select('//a[contains(@href, "nyaa")]/text()').extract()
      	result ['torrent'] = entries.select('//a[contains(@href,"download")]/@href').extract()
      	results.append(result)
    return result
'''