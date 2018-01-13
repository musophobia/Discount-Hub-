# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    old_price = scrapy.Field()
    new_price = scrapy.Field()
    percentage = scrapy.Field()
    url = scrapy.Field()
