from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy_sample.items import ScrapySampleItem

class ScrapyOrgSpider(BaseSpider):
	name = "scrapy"
	allowed_domains = ["wordpress.com"]
	start_urls = ["http://maxwellfoxman.wordpress.com"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		next_page = hxs.select("/html/body[@class='home blog single-author highlander-enabled highlander-light infinite-scroll']/div[@id='container']/div[@id='contents']/div[@id='infinite-handle']/span/@href").extract()
		if next_page:
			yield Request(next_page[0], self.parse)

		posts = hxs.select("/html/body[@class='home blog single-author highlander-enabled highlander-light infinite-scroll']/div[@id='container']/div[@id='contents']/div[@id='post-110']/div[@class='main']")
		items = []
		for post in posts:
			item = ScrapySampleItem()
			item["title"] = post.select("/html/body[@class='home blog single-author highlander-enabled highlander-light infinite-scroll']/div[@id='container']/div[@id='contents']//div[@class='main']/h2[@class='entry-title']/a/text()").extract()
			item["link"] = post.select("/html/body[@class='home blog single-author highlander-enabled highlander-light infinite-scroll']/div[@id='container']/div[@id='contents']//div[@class='main']/h2[@class='entry-title']/a/@href").extract()
			item["content"] = post.select("/html/body[@class='home blog single-author highlander-enabled highlander-light infinite-scroll']/div[@id='container']/div[@id='contents']//div[@class='main']/div[@class='entry-content']/p/text()").extract()
			items.append(item)
		for item in items:
			yield item