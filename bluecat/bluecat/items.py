# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BluecatItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GOODS_NAME = scrapy.Field()  # 商品名称
    GOODS_PRICE = scrapy.Field()  # 价格
    MONTHLY_SALES = scrapy.Field()  # 月销量
    GOODS_URL = scrapy.Field()  # 商品

