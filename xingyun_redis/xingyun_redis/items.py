# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XingyunRedisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 信息列表
    # list = scrapy.Field()
    #公司
    company= scrapy.Field()
    # 详情页地址
    # detail_url = scrapy.Field()
    # 经营范围
    # zone= scrapy.Field()
    # 当前企业状态
    status = scrapy.Field()
    # 老板
    boss = scrapy.Field()
    # 邮箱
    email = scrapy.Field()
    # 电话
    phone = scrapy.Field()
    # 地址
    address = scrapy.Field()
  