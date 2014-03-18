from scrapy.spider import Spider
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


from gumtree.items import GumtreeItem
count = 0
class GumtreeSpider(CrawlSpider):
    name = "gumtree"
    allowed_domains = ["gumtree.com.au"]
    start_urls = [
        "http://www.gumtree.com.au/s-bicycles/melbourne/c18560l3001317r50"
    ]

    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//div[@class="rs-paginator-pager"]/a[@class="rs-paginator-btn next"]', )), callback="parse_items", follow=True),)

    def parse_items(self, response):
        sel = Selector(response)
        ads = sel.xpath("//ul/li[@class='js-click-block ']")
        items = []
        global count
        if count < 100:
            for ad in ads:
                item = GumtreeItem()
                item['title'] = ad.xpath('div/div/h3[starts-with(@class, "rs-ad-title")]/a/text()').extract()[0].title()
                item['link'] = ad.xpath('div/div/h3[starts-with(@class, "rs-ad-title")]/a/@href').extract()[0]
                item['price'] = ad.xpath('div/div/div[contains(@class, "rs-ad-price")]/div[@class="h-elips "]/text()').extract()[0].strip()
                try:
                    item['pic'] = ad.xpath('div/div/div/img/@src').extract()[0]
                except IndexError:
                    item['pic'] = []
                try:
                    item['location'] = ad.xpath('div/div/span[@class="rs-ad-location-suburb"]/text()').extract()[0]
                except IndexError:
                    item['location'] = []
                items.append(item)
                count += 1
        return items
