from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mfitem.items import MfitemItem


class MySpider(BaseSpider):
    name = "max"
    allowed_domains = ["wordpress.com"]
    start_urls = ["http://maxwellfoxman.wordpress.com"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        items = []
        for titles in titles:
            item = MfitemItem()
            item ["title"] = titles.select("a/text()").extract()
            item ["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items