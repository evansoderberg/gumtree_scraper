from scrapy.spider import Spider
from scrapy.selector import Selector

from gumtree.items import GumtreeItem

class GumtreeSpider(Spider):
    name = "gumtree"
    allowed_domains = ["gumtree.com.au"]
    start_urls = [
        "http://www.gumtree.com.au/s-bicycles/melbourne/c18560l3001317r50"
    ]

    def parse(self, response):
        sel = Selector(response)
        ads = sel.xpath("//ul/li[@class='js-click-block ']")
        items = []
        for ad in ads:
            item = GumtreeItem()
            item['title'] = ad.xpath('div/div/h3[starts-with(@class, "rs-ad-title")]/a/text()').extract()[0].title()
            item['link'] = ad.xpath('div/div/h3[starts-with(@class, "rs-ad-title")]/a/@href').extract()[0]
            item['pic'] = ad.xpath('div/div/div/img/@src').extract()[0]
            try:
                item['location'] = ad.xpath('div/div/span[@class="rs-ad-location-suburb"]/text()').extract()
            except IndexError:
                item['location'] = []
            items.append(item)
        return items
