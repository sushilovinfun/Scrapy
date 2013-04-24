from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from bodytest.items import BodytestItem

class MySpider(BaseSpider):
    name = "bodytest3"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewtopic.php?f=17&t=6769"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        i = 0
        x = '//table[%d]/tr[2]/td[2]/table/tr/td/div/text()'
        items = []
        item = BodytestItem()
        
        while i < 6:
            y = x % i
            item ["body"] = hxs.select(y).extract()
            items.append(item)
            i = i + 1
        return items