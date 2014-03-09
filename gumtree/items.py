from scrapy.item import Item, Field

class GumtreeItem(Item):
    title = Field()
    link = Field()
    pic = Field()
    location = Field()
    price = Field()
