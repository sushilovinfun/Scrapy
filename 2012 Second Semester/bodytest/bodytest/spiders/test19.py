from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bodytest.items import BodytestItem

#Manual scrape News section

class MySpider(CrawlSpider):
    name = "news"
    allowed_domains = ["genofond.org"]
    start_urls = [
        "http://genofond.org/viewtopic.php?f=8&t=6676",
        "http://genofond.org/viewtopic.php?f=8&t=292",
        "http://genofond.org/viewtopic.php?f=8&t=6410",
        "http://genofond.org/viewtopic.php?f=8&t=6787",
        "http://genofond.org/viewtopic.php?f=8&t=6569",
        "http://genofond.org/viewtopic.php?f=8&t=49",
        "http://genofond.org/viewtopic.php?f=8&t=6596",
        "http://genofond.org/viewtopic.php?f=8&t=4625",
        "http://genofond.org/viewtopic.php?f=8&t=6753",
        "http://genofond.org/viewtopic.php?f=8&t=6670",
        "http://genofond.org/viewtopic.php?f=8&t=801",
        "http://genofond.org/viewtopic.php?f=8&t=196",
        "http://genofond.org/viewtopic.php?f=8&t=6786",
        "http://genofond.org/viewtopic.php?f=8&t=6414",
        "http://genofond.org/viewtopic.php?f=8&t=6663",
        "http://genofond.org/viewtopic.php?f=8&t=6661",
        "http://genofond.org/viewtopic.php?f=8&t=6605",
        "http://genofond.org/viewtopic.php?f=8&t=3205",
        "http://genofond.org/viewtopic.php?f=8&t=93",
        "http://genofond.org/viewtopic.php?f=8&t=6480",
        "http://genofond.org/viewtopic.php?f=8&t=6391",
        "http://genofond.org/viewtopic.php?f=8&t=6470",
        "http://genofond.org/viewtopic.php?f=8&t=6373",
        "http://genofond.org/viewtopic.php?f=8&t=1129",
        "http://genofond.org/viewtopic.php?f=8&t=839",
        "http://genofond.org/viewtopic.php?f=8&t=4155",
        "http://genofond.org/viewtopic.php?f=8&t=684",
        "http://genofond.org/viewtopic.php?f=8&t=6227",
        "http://genofond.org/viewtopic.php?f=8&t=6218",
        "http://genofond.org/viewtopic.php?f=8&t=5205",
        "http://genofond.org/viewtopic.php?f=8&t=789",
        "http://genofond.org/viewtopic.php?f=8&t=851",
        "http://genofond.org/viewtopic.php?f=8&t=835",
        "http://genofond.org/viewtopic.php?f=8&t=825",
        "http://genofond.org/viewtopic.php?f=8&t=819",
        "http://genofond.org/viewtopic.php?f=8&t=817",
        "http://genofond.org/viewtopic.php?f=8&t=803",
        "http://genofond.org/viewtopic.php?f=8&t=788",
        "http://genofond.org/viewtopic.php?f=8&t=716",
        "http://genofond.org/viewtopic.php?f=8&t=197",
        "http://genofond.org/viewtopic.php?f=8&t=757",
        "http://genofond.org/viewtopic.php?f=8&t=714",
        "http://genofond.org/viewtopic.php?f=8&t=710",
        "http://genofond.org/viewtopic.php?f=8&t=711",
        "http://genofond.org/viewtopic.php?f=8&t=121",
        "http://genofond.org/viewtopic.php?f=8&t=702",
        "http://genofond.org/viewtopic.php?f=8&t=688",
        "http://genofond.org/viewtopic.php?f=8&t=682",
        "http://genofond.org/viewtopic.php?f=8&t=679",
        "http://genofond.org/viewtopic.php?f=8&t=677",
        "http://genofond.org/viewtopic.php?f=8&t=661",
        "http://genofond.org/viewtopic.php?f=8&t=169",
        "http://genofond.org/viewtopic.php?f=8&t=304",
        "http://genofond.org/viewtopic.php?f=8&t=131",
        "http://genofond.org/viewtopic.php?f=8&t=163",
        "http://genofond.org/viewtopic.php?f=8&t=21",
        "http://genofond.org/viewtopic.php?f=8&t=107",
        "http://genofond.org/viewtopic.php?f=8&t=91",
        "http://genofond.org/viewtopic.php?f=8&t=40",
        "http://genofond.org/viewtopic.php?f=8&t=47",
        "http://genofond.org/viewtopic.php?f=8&t=62",
        "http://genofond.org/viewtopic.php?f=8&t=58",
        "http://genofond.org/viewtopic.php?f=8&t=55",
        "http://genofond.org/viewtopic.php?f=8&t=18",
        "http://genofond.org/viewtopic.php?f=8&t=45",
        "http://genofond.org/viewtopic.php?f=8&t=27",
        "http://genofond.org/viewtopic.php?f=8&t=35",
        "http://genofond.org/viewtopic.php?f=8&t=31",
        "http://genofond.org/viewtopic.php?f=8&t=24",
        "http://genofond.org/viewtopic.php?f=8&t=23",
        "http://genofond.org/viewtopic.php?f=8&t=22",
        "http://genofond.org/viewtopic.php?f=8&t=11",
        "http://genofond.org/viewtopic.php?f=8&t=10",
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