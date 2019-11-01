# -*- coding: utf-8 -*-
import scrapy
import random
from lxml import etree
import requests
from scrapy_redis.spiders import RedisSpider
from xingyun_redis.items import XingyunRedisItem


class MoviesSpider(RedisSpider):
    name = 'MovieSpider'
    allowed_domains = ['qichacha.com']
    url_list = []
    list_other = []
    print(2)
    redis_key = 'MovieSpider:start_urls'


    def parse(self,response):
        html=etree.HTML(response.text)
        # print(response.text)
        case_url=html.xpath("//section[@id='searchlist']/table/tbody/tr")
        for i in case_url:
            detail_url="https://www.qichacha.com"+i.xpath(".//td[2]/a/@href")[0]
            # print(detail_url)
            # print("*"*20)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail, dont_filter=True)
    def parse_detail(self, response):
        # print(response.text)
        # with open("w.html","a+",encoding="utf-8",)as f:
        #     f.write(response.text)
        item = XingyunRedisItem()
        rep = etree.HTML(response.text)
        case1 = rep.xpath("//div[@id='company-top']/div[@class='row']/div[@class='content']")
        # print(case1)
        # print("*"*20)
        # case2= rep.xpath("//section[@id='Cominfo']")
        # print(1)
        for inf1 in case1:
            # print(200)
            item["company"] = inf1.xpath(".//div[@class='row title jk-tip']/h1/text()")[0].strip()
            item["status"] = inf1.xpath(".//div[@class='row tags']/span[@class='ntag text-success tooltip-br']/text()")[0].strip()
            # if len(status)==0:
            #     item["status"]="mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            # else:
            #     item["status"] = inf1.xpath(".//div[@class='row tags']/span/text()")[0].strip()

            item["phone"] = inf1.xpath(".//div[@class='dcontent']/div[1]/span[1]/span[2]/text()")[0].strip()
            # if len(phone) == 0:
            #     item["phone"] = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            # else:
            #     item["phone"] =inf1.xpath(".//div[@class='dcontent']/div[1]/span[1]/span[2]/text()")[0].strip()

            item["email"]= inf1.xpath(".//div[@class='dcontent']/div[2]/span[1]/span[2]/text()")[0].strip()
            # if len(email) == 0:
            #     item["email"] = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            # else:
            #     item["email"] = inf1.xpath(".//div[@class='dcontent']/div[2]/span[1]/span[2]/text()")[0].strip()


            item["address"] = inf1.xpath(".//div[@class='dcontent']/div[2]/span[last()]/a[1]/text()")[0].strip()
            # if len(address) == 0:
            #     item["address"] = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            # else:
            #     item["address"] =inf1.xpath(".//div[@class='dcontent']/div[2]/span[last()]/a[1]/text()")[0].strip()


            
            # if len(company) == 0:
            #     item["company"] = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
            # else:
            #     item["company"] = inf1.xpath(".//div[@class='row title jk-tip']/h1/text()")[0].strip()
        yield item
        # for inf2 in case2:
        #     item["boss"] = inf2.xpath(".//a[@class='bname']/h2/text()")[0].strip()
        #     item["zone"] = inf2.xpath('//td[contains(text(),"经营范围")]/following-sibling::td[1]')[0]
        #     yield item

      
        
        




