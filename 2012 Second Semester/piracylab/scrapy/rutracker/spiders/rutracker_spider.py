from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from rutracker.items import rtItem

class rtSpider(CrawlSpider):
    name = 'rutracker.org'
    allowed_domains = ['rutracker.org']
    
    # start from the sociology forum
    start_urls = ['http://rutracker.org/forum/viewforum.php?f=2471']
    
    # set rules for only crawling the forum's "next page" links and topic links
    rules = (
            # extract and follow the forum's page links
            Rule(SgmlLinkExtractor(restrict_xpaths="//div[@id='pagination']/p[@style='float: right']")),
            # extract the topic links and scrape data from them
            Rule(SgmlLinkExtractor(restrict_xpaths="//tr[@class='hl-tr']/td[2]"), 
            callback='parse_topic'),
            )
       
    # extracts the information from a scraped topic page     
    def parse_topic(self, response):
        x = HtmlXPathSelector(response)
        # get the list of posters
        posters = x.select("//p[@class='nick']/text()").extract()
        # set the first in list of posters as topic author
        op = posters[0]
        # get the topic url and title
        url = response.url
        title = x.select("//h1[@class='maintitle']/a/text()").extract()
        # go through list of posters and remove any duplicates
        topicbody = x.select("//td[@class='message td2']/div/div/text()").extract()
        posters_export = [op]
        for p in posters:
            if (p not in posters_export):
                posters_export.append(p)
        # create an item for each unique poster in the topic
        topics = []
        for pe in posters_export:
            topic = rtItem()
            topic['topic_url'] = url
            topic['topic_title'] = title
            topic['post_author'] = op
            topic['poster'] = pe
            topic['topicbody'] = topicbody
            topics.append(topic)
            
        return topics