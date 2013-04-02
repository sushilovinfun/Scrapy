from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy_sample.items import ScrapySampleItem

class ScrapyOrgSpider(BaseSpider):
	name = "scrapy"
	allowed_domains = ["bushwickdaily.com"]
	start_urls = ["http://www.bushwickdaily.com/"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		next_page = hxs.select("//div[@id='main']/div[@class='wrapper group']/div[@id='columns']/div[@id='column-center']/div[@id='center-content']/div[@id='page-buttons']/a[@class='page-button-older']/@href").extract()
		if not not next_page:
			yield Request(next_page[0], self.parse)

		title = hxs.select("/html/body/div[2]/div/div[2]/div[2]/div/div/h2/a/text()").extract()

		content = hxs.select("//div[@class='entry']/p/text()").extract()
		#this parses through the center content of the page
		items = []
		for item in title:
			item = ScrapySampleItem()
			item["title"] = title
			item["content"] = content
			items.append(item)
		
		yield items