from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bodytest.items import BodytestItem

#Another attempt at the XPath. This will call up the last 4 pages and the first page of every page.
#What is interesting about this is that it was actually following, of all things the links under each section link (look at the start_url to see what I mean)

class MySpider(CrawlSpider):
    name = "bodytest8"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewforum.php?f=17"]

    rules = (# extract and follow the forum's page links
            Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='pagecontent']/table[1]/tr/td[4]/b/a[4]")),
            # extract the topic links and scrape data from them
            Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='pagecontent']/table[2]/tr/td[3]/a"), callback='parse_topic'),
            Rule(SgmlLinkExtractor(allow='.&t=\S+&start=\d+'), callback='parse_topic', follow=True),
            ) 
    #follow=True at the end?

    #changed to parse_start_url to scrape the first page and onwards... UNSURE if it is necessary to do for final code
    def parse_topic(self, response):
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