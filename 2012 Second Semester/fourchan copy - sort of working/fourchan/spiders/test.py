from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from fourchan.items import FourchanItem


class MySpider(CrawlSpider):
    name = "chan"
    allowed_domains = ["4chan.org"]
    start_urls = ["http://boards.4chan.org/asp/"]

    rules = (Rule(SgmlLinkExtractor(allow=('.\d+')), callback="parse_items", follow=True), )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        
        titles = hxs.select("/html/body")
        items = []
        for titles in titles:
            item = FourchanItem()
            item ["text"] = titles.select("/html/body/form/div/div/div/div/div/span[@class='subject']/text()").extract()
            item ["author"] = titles.select("/html/body/form/div/div/div/div/div/span[@class='nameBlock']/span/text()").extract()
            item ["datetime"] = titles.select("/html/body/form/div/div/div/div/div/span[@class='dateTime']/text()").extract()
            item ["body"] = titles.select("/html/body/form/div/div/div/div/blockquote/text()").extract()
            items.append(item)
        return items