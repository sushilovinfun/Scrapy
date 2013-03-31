# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class WikilongcrawlItem(Item):
    title = Field()# define the fields for your item here like:
    subs = Field()# name = Field()
    pass
