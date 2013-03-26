from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://maxwellfoxman.wordpress.com/2013/02/02/the-techne-of-memory-conversations-on-how-memory-is-brought-forth/",
        "http://maxwellfoxman.wordpress.com/2012/12/06/the-sacred-and-the-transgressive/", "http://maxwellfoxman.wordpress.com/2012/09/18/observations-on-sun-and-sea/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)