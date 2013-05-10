from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from bodytest.items import BodytestItem

#This scrapes just the text of the first paragraph of a single link. I believe this
#was an experiment in trying to locate the postbody. Final XPath was - "//div[@class='postbody']"

class MySpider(BaseSpider):
    name = "bodytest2"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewtopic.php?f=17&t=6769"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//table[4]/tr[2]/td[2]/table/tr/td/div/text()").extract()
        items = []
        for titles in titles:
            item = BodytestItem()
            item ["body"] = titles
            items.append(item)
        return items