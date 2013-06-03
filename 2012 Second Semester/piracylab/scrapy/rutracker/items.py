# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class rtItem(Item):
    post_author = Field()
    poster = Field()
    #forum_id = Field()
    #forum_name = Field()
    topic_url = Field()
    topic_title = Field()
    topicbody = Field()
    #topic_date = Field()
    #torrent = Field() # data here indicates this was a seeder
