from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mfitem.items import MfitemItem


class MySpider(BaseSpider):
    name = "sub"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Archive"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("/html/body")
        items = []
        for titles in titles:
            item = MfitemItem()
            item ["subs"] = titles.select("/html/body/div/div/div/h3/span/text()").extract()
            items.append(item)
        return items