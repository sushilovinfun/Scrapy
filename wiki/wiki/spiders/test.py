from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from wiki.items import WikiItem


class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Archive"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        items = []
        for titles in titles:
            item = WikiItem()
            item ["title"] = titles.select("a/text()").extract()
            item ["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items