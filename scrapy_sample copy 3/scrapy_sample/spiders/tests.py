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

		posts = hxs.select("//div[@id='center-content']")
		items = []
		for post in posts:
			item = ScrapySampleItem()
			item["title"] = post.select("//div[@id='main']/div[@class='wrapper group']/div[@id='columns']/div[@id='column-center']/div[@id='center-content']/div[@class='post group']/h2[@class='post-head']/a/text()").extract()
			item["link"] = post.select("//div[@id='main']/div[@class='wrapper group']/div[@id='columns']/div[@id='column-center']/div[@id='center-content']/div[@class='post group']/h2[@class='post-head']/a/@href").extract()
			item["content"] = post.select("//div[@id='main']/div[@class='wrapper group']/div[@id='columns']/div[@id='column-center']/div[@id='center-content']/div[@class='post group']/div[@class='entry']/p/text()").extract()
			items.append(item)
		for item in items:
			yield item