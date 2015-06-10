# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class RealtyItem(Item):

    name = Field()
    description = Field()
    url = Field()
    price = Field()
    floor = Field()
    space = Field()
    kitchen = Field()
