from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bodytest.items import BodytestItem

#Manual scrape of Library Things

class MySpider(CrawlSpider):
    name = "bodytest17"
    allowed_domains = ["genofond.org"]
    start_urls = [
        "http://genofond.org/viewtopic.php?f=17&t=1037",
        "http://genofond.org/viewtopic.php?f=17&t=6417",
        "http://genofond.org/viewtopic.php?f=17&t=6842",
        "http://genofond.org/viewtopic.php?f=17&t=104",
        "http://genofond.org/viewtopic.php?f=17&t=777",
        "http://genofond.org/viewtopic.php?f=17&t=6462",
        "http://genofond.org/viewtopic.php?f=17&t=6727",
        "http://genofond.org/viewtopic.php?f=17&t=6770",
        "http://genofond.org/viewtopic.php?f=17&t=6721",
        "http://genofond.org/viewtopic.php?f=17&t=607",
        "http://genofond.org/viewtopic.php?f=17&t=6785",
        "http://genofond.org/viewtopic.php?f=17&t=6862",
        "http://genofond.org/viewtopic.php?f=17&t=6836",
        "http://genofond.org/viewtopic.php?f=17&t=1079",
        "http://genofond.org/viewtopic.php?f=17&t=5943",
        "http://genofond.org/viewtopic.php?f=17&t=709",
        "http://genofond.org/viewtopic.php?f=17&t=20",
        "http://genofond.org/viewtopic.php?f=17&t=6832",
        "http://genofond.org/viewtopic.php?f=17&t=6825",
        "http://genofond.org/viewtopic.php?f=17&t=6734",
        "http://genofond.org/viewtopic.php?f=17&t=6800",
        "http://genofond.org/viewtopic.php?f=17&t=6795",
        "http://genofond.org/viewtopic.php?f=17&t=6732",
        "http://genofond.org/viewtopic.php?f=17&t=6424",
        "http://genofond.org/viewtopic.php?f=17&t=6768",
        "http://genofond.org/viewtopic.php?f=17&t=6738",
        "http://genofond.org/viewtopic.php?f=17&t=6705",
        "http://genofond.org/viewtopic.php?f=17&t=663",
        "http://genofond.org/viewtopic.php?f=17&t=849",
        "http://genofond.org/viewtopic.php?f=17&t=6697",
        "http://genofond.org/viewtopic.php?f=17&t=5623",
        "http://genofond.org/viewtopic.php?f=17&t=6449",
        "http://genofond.org/viewtopic.php?f=17&t=6432",
        "http://genofond.org/viewtopic.php?f=17&t=6406",
        "http://genofond.org/viewtopic.php?f=17&t=6392",
        "http://genofond.org/viewtopic.php?f=17&t=3287",
        "http://genofond.org/viewtopic.php?f=17&t=823",
        "http://genofond.org/viewtopic.php?f=17&t=786",
        "http://genofond.org/viewtopic.php?f=17&t=845",
        "http://genofond.org/viewtopic.php?f=17&t=299",
        "http://genofond.org/viewtopic.php?f=17&t=815",
        "http://genofond.org/viewtopic.php?f=17&t=821",
        "http://genofond.org/viewtopic.php?f=17&t=734",
        "http://genofond.org/viewtopic.php?f=17&t=781",
        "http://genofond.org/viewtopic.php?f=17&t=680",
        "http://genofond.org/viewtopic.php?f=17&t=678",
        "http://genofond.org/viewtopic.php?f=17&t=597",
        "http://genofond.org/viewtopic.php?f=17&t=157",
        "http://genofond.org/viewtopic.php?f=17&t=669",
        "http://genofond.org/viewtopic.php?f=17&t=667",
        "http://genofond.org/viewtopic.php?f=17&t=658",
        "http://genofond.org/viewtopic.php?f=17&t=296",
        "http://genofond.org/viewtopic.php?f=17&t=574",
        "http://genofond.org/viewtopic.php?f=17&t=344",
        "http://genofond.org/viewtopic.php?f=17&t=531",
        "http://genofond.org/viewtopic.php?f=17&t=474",
        "http://genofond.org/viewtopic.php?f=17&t=417",
        "http://genofond.org/viewtopic.php?f=17&t=382",
        "http://genofond.org/viewtopic.php?f=17&t=358",
        "http://genofond.org/viewtopic.php?f=17&t=294",
        "http://genofond.org/viewtopic.php?f=17&t=69",
        "http://genofond.org/viewtopic.php?f=17&t=64",

    ]

    rules = (
            Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='pagecontent']/table[29]/tr/td[4]/b/a"), callback='parse_start_url', follow=True), )

    #changed to parse_start_url to scrape the first page and onwards... UNSURE if it is necessary to do for final code
    def parse_start_url(self, response):
        x = HtmlXPathSelector(response)
        # get the list of posters
        posters = x.select("//b[@class='postauthor']/text()").extract()
        # set the first in list of posters as topic author
        op = posters[0]
        # get the topic url and title
        url = response.url

        title = x.select("//div[@id='pageheader']/h2/a/text()").extract()

        #scrape topic body 
        #But this scrape is not quite working. It is posting 
        #the entire body of the page and not just the specific loop.
        #I am not sure why at all
        post_body = x.select("//div[@class='postbody']").extract()

        # go through list of posters and remove any duplicates
        posters_export = [op]
        for p in posters:
                posters_export.append(p)
        # create an item for each unique poster in the topic
        topics = []
        for i, pb in enumerate(post_body):
            topic = BodytestItem()
            topic['topic_url'] = url
            topic['topic_title'] = title
            topic['thread_author'] = op
            topic['post_author'] = posters[i]
            topic['post_body'] = pb
            topics.append(topic)

        return topics