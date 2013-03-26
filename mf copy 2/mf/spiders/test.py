from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mf.items import MfItem


class MySpider(BaseSpider):
    name = "mf"
    allowed_domains = ["wordpress.com"]
    start_urls = ["http://maxwellfoxman.wordpress.com"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        descs = hxs.select("/html/body/div/div[3]/div/div[2]/h2/a/text()")
        bodies = hxs.select("//p/text()")
        for descs in descs:
            desc = descs.extract()
            print desc
        for bodies in bodies:
            body = bodies.extract()
            print body

