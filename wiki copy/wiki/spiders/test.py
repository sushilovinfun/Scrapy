from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from wiki.items import WikiItem


class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Archive"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        descs = hxs.select("/html/body/div[3]/div[2]/div[4]/p[2]/text()")
        for descs in descs:
            desc = descs.extract()
            print desc

