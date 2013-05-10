from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bodytest.items import BodytestItem

#Manual scrape of Freestyle Section

class MySpider(CrawlSpider):
    name = "freestyle2"
    allowed_domains = ["genofond.org"]
    start_urls = [
        "http://genofond.org/viewtopic.php?f=6&t=6228",
        "http://genofond.org/viewtopic.php?f=6&t=29",
        "http://genofond.org/viewtopic.php?f=6&t=598",
        "http://genofond.org/viewtopic.php?f=6&t=6860",
        "http://genofond.org/viewtopic.php?f=6&t=6850",
        "http://genofond.org/viewtopic.php?f=6&t=6852",
        "http://genofond.org/viewtopic.php?f=6&t=6788",
        "http://genofond.org/viewtopic.php?f=6&t=6784",
        "http://genofond.org/viewtopic.php?f=6&t=6799",
        "http://genofond.org/viewtopic.php?f=6&t=6397",
        "http://genofond.org/viewtopic.php?f=6&t=6541",
        "http://genofond.org/viewtopic.php?f=6&t=6455",
        "http://genofond.org/viewtopic.php?f=6&t=811",
        "http://genofond.org/viewtopic.php?f=6&t=6451",
        "http://genofond.org/viewtopic.php?f=6&t=6742",
        "http://genofond.org/viewtopic.php?f=6&t=6483",
        "http://genofond.org/viewtopic.php?f=6&t=6669",
        "http://genofond.org/viewtopic.php?f=6&t=6710",
        "http://genofond.org/viewtopic.php?f=6&t=6665",
        "http://genofond.org/viewtopic.php?f=6&t=6671",
        "http://genofond.org/viewtopic.php?f=6&t=744",
        "http://genofond.org/viewtopic.php?f=6&t=6683",
        "http://genofond.org/viewtopic.php?f=6&t=6415",
        "http://genofond.org/viewtopic.php?f=6&t=6485",
        "http://genofond.org/viewtopic.php?f=6&t=6474",
        "http://genofond.org/viewtopic.php?f=6&t=6477",
        "http://genofond.org/viewtopic.php?f=6&t=6471",
        "http://genofond.org/viewtopic.php?f=6&t=6467",
        "http://genofond.org/viewtopic.php?f=6&t=6457",
        "http://genofond.org/viewtopic.php?f=6&t=6453",
        "http://genofond.org/viewtopic.php?f=6&t=6431",
        "http://genofond.org/viewtopic.php?f=6&t=6443",
        "http://genofond.org/viewtopic.php?f=6&t=6444",
        "http://genofond.org/viewtopic.php?f=6&t=6437",
        "http://genofond.org/viewtopic.php?f=6&t=6438",
        "http://genofond.org/viewtopic.php?f=6&t=6371",
        "http://genofond.org/viewtopic.php?f=6&t=6396",
        "http://genofond.org/viewtopic.php?f=6&t=6422",
        "http://genofond.org/viewtopic.php?f=6&t=780",
        "http://genofond.org/viewtopic.php?f=6&t=6412",
        "http://genofond.org/viewtopic.php?f=6&t=6407",
        "http://genofond.org/viewtopic.php?f=6&t=6408",
        "http://genofond.org/viewtopic.php?f=6&t=805",
        "http://genofond.org/viewtopic.php?f=6&t=6401",
        "http://genofond.org/viewtopic.php?f=6&t=6358",
        "http://genofond.org/viewtopic.php?f=6&t=6167",
        "http://genofond.org/viewtopic.php?f=6&t=6384",
        "http://genofond.org/viewtopic.php?f=6&t=6360",
        "http://genofond.org/viewtopic.php?f=6&t=6329",
        "http://genofond.org/viewtopic.php?f=6&t=686",
        "http://genofond.org/viewtopic.php?f=6&t=6154",
        "http://genofond.org/viewtopic.php?f=6&t=5969",
        "http://genofond.org/viewtopic.php?f=6&t=5668",
        "http://genofond.org/viewtopic.php?f=6&t=5692",
        "http://genofond.org/viewtopic.php?f=6&t=5249",
        "http://genofond.org/viewtopic.php?f=6&t=4831",
        "http://genofond.org/viewtopic.php?f=6&t=690",
        "http://genofond.org/viewtopic.php?f=6&t=2529",
        "http://genofond.org/viewtopic.php?f=6&t=676",
        "http://genofond.org/viewtopic.php?f=6&t=1053",
        "http://genofond.org/viewtopic.php?f=6&t=1041",
        "http://genofond.org/viewtopic.php?f=6&t=689",
        "http://genofond.org/viewtopic.php?f=6&t=630",
        "http://genofond.org/viewtopic.php?f=6&t=795",
        "http://genofond.org/viewtopic.php?f=6&t=715",
        "http://genofond.org/viewtopic.php?f=6&t=758",
        "http://genofond.org/viewtopic.php?f=6&t=776",
        "http://genofond.org/viewtopic.php?f=6&t=782",
        "http://genofond.org/viewtopic.php?f=6&t=779",
        "http://genofond.org/viewtopic.php?f=6&t=778",
        "http://genofond.org/viewtopic.php?f=6&t=721",
        "http://genofond.org/viewtopic.php?f=6&t=685",
        "http://genofond.org/viewtopic.php?f=6&t=727",
        "http://genofond.org/viewtopic.php?f=6&t=717",
        "http://genofond.org/viewtopic.php?f=6&t=722",
        "http://genofond.org/viewtopic.php?f=6&t=719",
        "http://genofond.org/viewtopic.php?f=6&t=693",
        "http://genofond.org/viewtopic.php?f=6&t=696",
        "http://genofond.org/viewtopic.php?f=6&t=697",
        "http://genofond.org/viewtopic.php?f=6&t=698",
        "http://genofond.org/viewtopic.php?f=6&t=695",
        "http://genofond.org/viewtopic.php?f=6&t=691",
        "http://genofond.org/viewtopic.php?f=6&t=674",
        "http://genofond.org/viewtopic.php?f=6&t=671",
        "http://genofond.org/viewtopic.php?f=6&t=659",
        "http://genofond.org/viewtopic.php?f=6&t=627",
        "http://genofond.org/viewtopic.php?f=6&t=581",
        "http://genofond.org/viewtopic.php?f=6&t=515",
        "http://genofond.org/viewtopic.php?f=6&t=214",
        "http://genofond.org/viewtopic.php?f=6&t=418",
        "http://genofond.org/viewtopic.php?f=6&t=412",
        "http://genofond.org/viewtopic.php?f=6&t=339",
        "http://genofond.org/viewtopic.php?f=6&t=82",
        "http://genofond.org/viewtopic.php?f=6&t=293",
        "http://genofond.org/viewtopic.php?f=6&t=287",
        "http://genofond.org/viewtopic.php?f=6&t=275",
        "http://genofond.org/viewtopic.php?f=6&t=217",
        "http://genofond.org/viewtopic.php?f=6&t=251",
        "http://genofond.org/viewtopic.php?f=6&t=109",
        "http://genofond.org/viewtopic.php?f=6&t=245",
        "http://genofond.org/viewtopic.php?f=6&t=230",
        "http://genofond.org/viewtopic.php?f=6&t=241",
        "http://genofond.org/viewtopic.php?f=6&t=240",
        "http://genofond.org/viewtopic.php?f=6&t=223",
        "http://genofond.org/viewtopic.php?f=6&t=224",
        "http://genofond.org/viewtopic.php?f=6&t=218",
        "http://genofond.org/viewtopic.php?f=6&t=215",
        "http://genofond.org/viewtopic.php?f=6&t=212",
        "http://genofond.org/viewtopic.php?f=6&t=153",
        "http://genofond.org/viewtopic.php?f=6&t=110",
        "http://genofond.org/viewtopic.php?f=6&t=114",
        "http://genofond.org/viewtopic.php?f=6&t=190",
        "http://genofond.org/viewtopic.php?f=6&t=156",
        "http://genofond.org/viewtopic.php?f=6&t=188",
        "http://genofond.org/viewtopic.php?f=6&t=185",
        "http://genofond.org/viewtopic.php?f=6&t=184",
        "http://genofond.org/viewtopic.php?f=6&t=182",
        "http://genofond.org/viewtopic.php?f=6&t=174",
        "http://genofond.org/viewtopic.php?f=6&t=172",
        "http://genofond.org/viewtopic.php?f=6&t=170",
        "http://genofond.org/viewtopic.php?f=6&t=159",
        "http://genofond.org/viewtopic.php?f=6&t=158",
        "http://genofond.org/viewtopic.php?f=6&t=152",
        "http://genofond.org/viewtopic.php?f=6&t=143",
        "http://genofond.org/viewtopic.php?f=6&t=128",
        "http://genofond.org/viewtopic.php?f=6&t=137",
        "http://genofond.org/viewtopic.php?f=6&t=117",
        "http://genofond.org/viewtopic.php?f=6&t=90",
        "http://genofond.org/viewtopic.php?f=6&t=116",
        "http://genofond.org/viewtopic.php?f=6&t=78",
        "http://genofond.org/viewtopic.php?f=6&t=99",
        "http://genofond.org/viewtopic.php?f=6&t=101",
        "http://genofond.org/viewtopic.php?f=6&t=79",
        "http://genofond.org/viewtopic.php?f=6&t=85",
        "http://genofond.org/viewtopic.php?f=6&t=70",
        "http://genofond.org/viewtopic.php?f=6&t=68",
        "http://genofond.org/viewtopic.php?f=6&t=67",
        "http://genofond.org/viewtopic.php?f=6&t=66",
        "http://genofond.org/viewtopic.php?f=6&t=56",
        "http://genofond.org/viewtopic.php?f=6&t=26",

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