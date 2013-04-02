# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FourchanItem(Item):
    text = Field() 
    author = Field()# define the fields for your item here like:
    datetime = Field()# name = Field()
    body = Field()
    pass
