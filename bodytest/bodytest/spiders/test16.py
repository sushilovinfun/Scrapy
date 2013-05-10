from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bodytest.items import BodytestItem

class MySpider(CrawlSpider):
    name = "bodytest16"
    allowed_domains = ["genofond.org"]
    start_urls = [
        "http://genofond.org/viewtopic.php?f=9&t=123",
        "http://genofond.org/viewtopic.php?f=9&t=6452",
        "http://genofond.org/viewtopic.php?f=9&t=6428",
        "http://genofond.org/viewtopic.php?f=9&t=6694",
        "http://genofond.org/viewtopic.php?f=9&t=3249",
        "http://genofond.org/viewtopic.php?f=9&t=6563",
        "http://genofond.org/viewtopic.php?f=9&t=122",
        "http://genofond.org/viewtopic.php?f=9&t=127",
        "http://genofond.org/viewtopic.php?f=9&t=6567",
        "http://genofond.org/viewtopic.php?f=9&t=6491",
        "http://genofond.org/viewtopic.php?f=9&t=6475",
        "http://genofond.org/viewtopic.php?f=9&t=6479",
        "http://genofond.org/viewtopic.php?f=9&t=106",
        "http://genofond.org/viewtopic.php?f=9&t=298",

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