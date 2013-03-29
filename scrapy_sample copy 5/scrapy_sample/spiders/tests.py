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
		#this parses through the center content of the page
		items = []
		for post in posts:
			item = ScrapySampleItem()
			item["title"] = post.select("//div[@id='center-content']/div/h2/a/text()").extract() #parses the title of posts
			item["link"] = post.select("//div[@id='center-content']/div/h2/a/@href").extract() #parses the affiliated link
			item["content"] = post.select("//div[@id='center-content']/div/div/p/text()").extract() #parses the content of the page
			item["meta"] = post.select("//div[@id='center-content']/div/p/text()").extract() #parses the meta section of date, etc.
			item["author"]= post.select("//span[@class='written']/a/text()").extract() #parses the author in that section
			item["section"] = post.select("//div[@id='center-content']/div/p[@class='category-text']/a/text()").extract() #says the affiliated sections
			items.append(item)
		for item in items:
			yield item