from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from arnet.items import ArnetItem

class MySpider(CrawlSpider):
    name = "arnet2"
    allowed_domains = ["arnetminer.org"]
    
    start_urls = [
    	"http://arnetminer.org/person/usama-m-fayyad-157717.html",
    ]

    def parse(self, response):
    	x= HtmlXPathSelector(response)
        
        titles = x.select("/html/body")
        items = []
        for titles in titles:
            item = ArnetItem()
            item ["Name"] = titles.select("//*[@id='contentZone']/div[1]/div[1]/h1/text()").extract()
            item ["Current_Title"] = titles.select("//*[@id='contentZone']/div[3]/dl/dd[1]/text()").extract()
            item ["Affiliation"] = titles.select("//*[@id='contentZone']/div[3]/dl/dd[2]/text()").extract()
            item ["Bio"] = titles.select("//*[@id='contentZone_0']/div[2]/p/text()").extract()
            item ["Education"] = titles.select("//*[@id='contentZone_1']/table/tr").extract()
            item ["Conferences"] = titles.select("//div[5]/div/div[2]/dl/dd/a[@class='label label-infox label-link']/text()").extract()
            items.append(item)
        return items