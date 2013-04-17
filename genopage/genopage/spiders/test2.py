from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from genopage.items import GenopageItem


class MySpider(BaseSpider):
    name = "genopage"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewtopic.php?f=17&sid=a4041d6dc62c565991c9d3d23b597830&t=6705"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("/html/body")
        items = []
        for titles in titles:
            item = GenopageItem()
            item ["poster"] = titles.select("//div[@id='pagecontent']/table[3]/tr[2]/td[1]/b/text()").extract()
            item ["title"] = titles.select("//div[@id='pagecontent']/table[3]/tr[2]/td[2]/table/tr/td/div[1]/text()").extract()
            item ["topicbody"] = titles.select("//div[@id='pagecontent']/table[3]/tr[3]/td[2]/table/tr/td/div/text()").extract()
            items.append(item)
        return items