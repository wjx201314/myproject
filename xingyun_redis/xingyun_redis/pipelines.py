# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class XingyunRedisPipeline(object):
#     def process_item(self, item, spider):
#         return item
# -*- coding: utf-8 -*-

# import pymysql
from scrapy.utils.project import get_project_settings
import re
import xlwt
import xlrd
from xlutils import copy
from redis import *
from scrapy.exceptions import DropItem


class XunyingPipeline(object):
    # # class DuplicatesPipeline(object):
    #     def __init__(self):
    #         self.company = set()
    # 
    #     def process_item(self, item, spider):
    #         company = item['company']
    #         if company in self.company:
    #             raise DropItem('{}已存在'.format(company))
    # 
    #         self.company.add(company)  ##这里换成你自己的item["#"]
    #         return item
    pass
