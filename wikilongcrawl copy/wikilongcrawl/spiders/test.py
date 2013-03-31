from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from wikilongcrawl.items import WikilongcrawlItem

class MySpider(CrawlSpider):
	name = "wiki"
	allowed_domains = ["en.wikipedia.org"]
	start_urls = ["http://en.wikipedia.org/wiki/Archive"]

	rules = (Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='mw-content-text']/ul/li/a",)), Rule(SgmlLinkExtractor(restrict_xpaths="/html/body"), callback="parse_items"),)

	def parse_items(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("/html/body")
		items = []
		for titles in titles:
			item = WikilongcrawlItem()
			item ["title"] = titles.select("//div/h1/span/text()").extract()
			item ["subs"] = titles.select("/html/body/div/div/div/h3/span/text()").extract()
			items.append(item)
		return items