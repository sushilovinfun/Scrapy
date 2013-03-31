from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from fourchan.items import FourchanItem


class MySpider(BaseSpider):
    name = "chan"
    allowed_domains = ["4chan.org"]
    start_urls = ["http://boards.4chan.org/asp/"]

#/html/body[@class='yotsuba_b_new ws hasGoogleVoiceExt']/div[@class='pagelist desktop']/div[@class='next']/form/input

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        titles = hxs.select("/html/body")
        items = []
        for titles in titles:
            item = FourchanItem()
            item ["text"] = titles.select("/html/body/form/div/div/div/div/div/span[@class='subject']/text()").extract()
            item ["author"] = titles.select("/html/body/form/div/div/div/div/div/span[@class='nameBlock']/span/text()").extract()
            item ["datetime"] = titles.select("/html/body/form/div/div/div/div/div/span[@class='dateTime']/text()").extract()
            item ["body"] = titles.select("/html/body/form/div/div/div/div/blockquote/text()").extract()
            items.append(item)
        return items