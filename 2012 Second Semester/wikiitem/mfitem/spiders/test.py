from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mfitem.items import MfitemItem


class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Archive"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("/html/body")
        items = []
        for titles in titles:
            item = MfitemItem()
            item ["title"] = titles.select("//div/h1/span/text()").extract()
            item ["text"] = titles.select("//div[@id='mw-content-text']/p/text()").extract()
            item ["menu"] = titles.select("//div/div/div/h2/span/text()").extract()
            item ["links"] = titles.select("//a/@href").extract()
            item ["subs"] = titles.select("/html/body/div/div/div/h3/span/text()").extract()
            item ["thumbcaps"] = titles.select("/html/body/div/div/div/div/div/div/text()").extract()
            items.append(item)
        return items