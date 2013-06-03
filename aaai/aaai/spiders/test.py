from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from aaai.items import aaaiItem

class MySpider(CrawlSpider):
    name = "aaai"
    allowed_domains = ["aaai.org"]
    
    start_urls = [
    	"https://www.aaai.org/Library/Workshops/ws93-02.php",
    	"https://www.aaai.org/Library/Workshops/ws94-03.php",
    ]

    def parse(self, response):
    	x = HtmlXPathSelector(response)

    	posters = x.select("//*[@id='box6']/div/p/i/text()").extract()

    	scrapes = []

    	for i in posters:
    		scrape = aaaiItem()
    		scrape['authors'] = i
    		scrapes.append(scrape)

    	return scrapes