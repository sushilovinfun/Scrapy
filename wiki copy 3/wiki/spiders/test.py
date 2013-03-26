from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from wiki.items import WikiItem


class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Archive"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        descs = hxs.select("/html/body/div[3]/div[2]/div[4]/h2/span[2]")
        #This seems to pull of text information about the text as well.
        for descs in descs:
            desc = descs.extract()
            print desc