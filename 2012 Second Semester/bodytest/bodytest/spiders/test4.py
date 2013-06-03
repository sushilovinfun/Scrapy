from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from bodytest.items import BodytestItem

#Here I tried the "node()" XPath. No luck.
#was an experiment in trying to locate the postbody. Final XPath was - "//div[@class='postbody']"

class MySpider(BaseSpider):
    name = "bodytest4"
    allowed_domains = []
    start_urls = ["file://localhost/Users/maxwellfoxman/Downloads/viewtopic.php.html"]

    def parse(self, response):
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
        post_body = x.select("//div[@class='postbody']/node()").extract()
        # go through list of posters and remove any duplicates
        posters_export = []
        for p in posters:
                posters_export.append(p)
        # create an item for each unique poster in the topic
        topics = []
        for pe in posters_export:
            topic = BodytestItem()
            topic['topic_url'] = url
            topic['topic_title'] = title
            topic['thread_author'] = op
            topic['post_author'] = pe
            topic['post_body'] = post_body
            topics.append(topic)

        return topics