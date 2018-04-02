# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyaEmailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 保存数据的时候，email代表邮箱，url代表链接
    email = scrapy.Field()
    url = scrapy.Field()
    pass
