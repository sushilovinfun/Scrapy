# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BodytestItem(Item):
	topic_url = Field() # define the fields for your item here like:
	topic_title = Field()
	thread_author = Field()
	post_author = Field()
	post_body = Field()# name = Field()
	pass