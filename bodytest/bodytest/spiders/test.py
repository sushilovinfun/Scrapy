from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from bodytest.items import BodytestItem

#It should be noted for this test that I had to separate and create a new list for post_bodies to get it to work.
#Also should be noted the importance of the post_body XPath.

class MySpider(BaseSpider):
    name = "bodytest"
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
        post_body = x.select("//div[@class='postbody']").extract()
        # go through list of posters and remove any duplicates
        posters_export = [op]
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
            topics.append(topic)

        for pb in post_body:
            topic = BodytestItem()
            topic['post_body'] = pb
            topics.append(topic)

        return topics