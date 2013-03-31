from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from bushwick.items import BushwickItem

class MySpider(BaseSpider):
    name = "bushwick"
    allowed_domains = ["bushwickdaily.com"]
    start_urls = ["http://bushwickdaily.com/2013/03/sunday-read-its-who-we-are-by-cat-agonis/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        next_page = hxs.select("//div[@class='post-button-holder']/div[@class='post-button-older-wrap']/a[@class='post-button-older']/@href").extract()
        if not not next_page:
            yield Request(next_page[0], self.parse)

        titles = hxs.select("//div[@id='center-content']")
        items = []
        for titles in titles:
            item = BushwickItem()
            item ["category"] = titles.select("//div[@class='post group']/p[@class='category-text']/a/text()").extract()
            item ["headline"] = titles.select("//div[@class='post group']/h2[@class='post-head']/text()").extract()
            item ["metatext"] = titles.select("div[@class='post group']/p[@class='meta-text']/text()").extract()
            item ["author"] = titles.select("//div[@class='post group']/p[@class='meta-text']/span[@class='written']/a/text()").extract()
            item ["body"] = titles.select("//div[@class='post group']/div[@class='entry']/p/text()").extract()
            item ["about"] = titles.select("//div[@class='post group']/div[@class='entry']/div[@class='wp-biographia-container-top']/div[@class='wp-biographia-text']/p/text()").extract()
            item ["tags"] = titles.select("//div[@class='post group']/div[@class='tags']/a/text()").extract()
            items.append(item)
        for item in items:
            yield item