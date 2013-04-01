from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from bushwick.items import BushwickItem

class MySpider(CrawlSpider):
    name = "bushwick"
    allowed_domains = ["bushwickdaily.com"]
    start_urls = ["http://bushwickdaily.com/"]

    rules = [Rule(SgmlLinkExtractor(allow=[r'\d{4}/\d{2}/\w+']), callback='parse_items', follow=True)]

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
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