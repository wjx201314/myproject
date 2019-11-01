# -*- coding: utf-8 -*-
#encoding=utf-8
import scrapy
from bluecat.items import BluecatItem

class TapTop(scrapy.Spider):
    name = 'TapTop'
    allowed_domains = ['detail.tmall.com','list.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?spm=875.7931836/B.subpannel2016040.19.z5JOIv&pos=1&cat=50024399&theme=663&acm=2016031437.1003.2.720502&scm=1003.2.2016031437.OTHER_1458241115467_720502']

    def parse(self,response):
        divs = response.xpath('//div[@id="J_ItemList"]/div')
        # print("items len = %d" %len(divs))
        for div in divs:
            item = BluecatItem()
            # 价格
            item['GOODS_PRICE'] = div.xpath('div/p[1]/em/text()').extract_first()
            # 月销量
            item['MONTHLY_SALES'] = div.xpath('.//p[@class="productStatus"]/span/em/text()').extract_first()
            # url
            good_url = div.xpath('div/div[2]/a[1]/@href').extract_first()
            if not 'http' in good_url:
                good_url = response.urljoin(good_url)
            item['GOODS_URL'] = good_url

            # 进入店里面
            yield scrapy.Request(url=good_url, meta={'item':item}, callback=self.detail_parse)
        next_page = response.urljoin(response.xpath('//a[@class="ui-page-next"]/@href').extract_first())
        yield scrapy.Request(url=next_page,callback=self.parse)

    def detail_parse(self,response):
        # 获取item
        item = response.meta['item']
        # 商品名称
        item['GOODS_NAME'] = response.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/a/text()').extract_first()
        yield item
        print("*"*20)
        print(item)