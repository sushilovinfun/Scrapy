# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ArnetItem(Item):
	Name = Field() # define the fields for your item here like:
	Current_Title = Field() 
	Affiliation = Field()
	Bio = Field()
	Education = Field()
	Conferences = Field() 
	#Consider adding papers afterward.

	# name = Field()
	pass
