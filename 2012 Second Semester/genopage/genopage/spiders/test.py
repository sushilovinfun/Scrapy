from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from genopage.items import GenopageItem


class MySpider(BaseSpider):
    name = "genopage1"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewtopic.php?f=17&t=6825"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("/html/body")
        items = []
        for titles in titles:
            item = GenopageItem()
            item ["poster"] = titles.select("//table[@class='tablebg'][2]/tr[@class='row1']/td[1]/b[@class='postauthor']/text()").extract()
            item ["title"] = titles.select("//table[@class='tablebg'][2]/tr[@class='row1'][1]/td[2]/table/tr/td[@class='gensmall']/div[1]/text()").extract()
            item ["topicbody"] = titles.select("//table[@class='tablebg'][2]/tr[@class='row1'][2]/td[2]/table/tr/td/div[@class='postbody']/text()").extract()
            items.append(item)
        return items