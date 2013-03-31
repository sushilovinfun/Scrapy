from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy_sample.items import ScrapySampleItem

class ScrapyOrgSpider(BaseSpider):
	name = "scrapy"
	allowed_domains = ["4chan.org"]
	start_urls = ["http://boards.4chan.org/asp/"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		next_page = hxs.select("/html/body/div[10]/div[3]/form/input/@href").extract()
		if not not next_page:
			yield Request(next_page[0], self.parse)

		posts = hxs.select("/html/body/form[2]/div")
		items = []
		for post in posts:
			item = ScrapySampleItem()
			item["post"] = post.select("/html/body/form[2]/div/div/div/div/p/text()").extract()
			item["response"] = post.select("/html/body/form[2]/div/div/text()").extract()
			items.append(item)
		for item in items:
			yield item