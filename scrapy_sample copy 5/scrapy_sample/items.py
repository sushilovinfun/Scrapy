# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapySampleItem(Item):
	title = Field()# define the fields for your item here like:
	link = Field()# name = Field()
	content = Field()
	meta = Field()
	section = Field()
	author = Field()
	pass
