from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from bodytest.items import BodytestItem

#This was a test of both the multiple pages on the thread and the multiple threads on a given page section. 
#It does not include the multiple pages of the section.
#This might have been one of the more successful scrapes, but I believe wouldn't scrape the first page, hence
#why I went to parse_start_url instead

class MySpider(CrawlSpider):
    name = "bodytest12"
    allowed_domains = ["genofond.org"]
    start_urls = ["http://genofond.org/viewforum.php?f=17"]

    rules = (
            # extract and follow the forum's page links
            Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='pagecontent']/table[2]/tr/td[3]")),
            Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='pagecontent']/table[29]/tr/td/b/a"), callback='parse_topic', follow=True),
            )

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