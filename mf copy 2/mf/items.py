# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class MfItem(Item):
	desc = Field() # define the fields for your item here like:
	body = Field() # name = Field()
	pass
