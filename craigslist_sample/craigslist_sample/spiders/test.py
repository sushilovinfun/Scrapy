from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://newyork.craigslist.org/zip/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("/html/body/blockquote[4]/p/span[2]")
        for titles in titles:
            title = titles.select("a/text()").extract()
            link = titles.select("a/@href").extract()
            print title, link