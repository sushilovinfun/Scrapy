from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from bodytest.items import BodytestItem

class MySpider(BaseSpider):
    name = "bodytest"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewtopic.php?f=17&t=6769"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//div[@class='postbody']/text()").extract()
        items = []
        for titles in titles:
            item = BodytestItem()
            item ["body"] = titles
            items.append(item)
        return items