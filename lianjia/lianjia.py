import requests
import random
from lxml import etree
from urllib import parse


s = requests.session()

def get_url(i):
    base_url="https://cd.lianjia.com/zufang/pg{}/#contentList".format(i)
    useragent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36"]
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "lianjia_uuid=81e75139-91f3-4c83-8a67-21433ba4c7a4; select_city=510100; all-lj=3d0b35ab17a07d475f1852d271de56f8; _smt_uid=5dbe711a.163a439a; UM_distinctid=16e2fe9cfdc18d-0349d9473b48b-7a1437-144000-16e2fe9cfdd12d; CNZZDATA1253492306=1463722667-1572761389-https%253A%252F%252Fwww.baidu.com%252F%7C1572761389; CNZZDATA1254525948=1471030715-1572761174-https%253A%252F%252Fwww.baidu.com%252F%7C1572761174; CNZZDATA1255633284=591677041-1572760667-https%253A%252F%252Fwww.baidu.com%252F%7C1572760667; CNZZDATA1255604082=1974437933-1572760526-https%253A%252F%252Fwww.baidu.com%252F%7C1572760526; _jzqa=1.299030258109334340.1572761883.1572761883.1572761883.1; _jzqc=1; _jzqy=1.1572761883.1572761883.1.jzqsr=baidu.-; _jzqckmp=1; _qzja=1.2107998316.1572761883133.1572761883133.1572761883133.1572761883133.1572761883133.0.0.0.1.1; _qzjc=1; _qzjto=1.1.0; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e2fe9d23f229-0410f1dfca8cbc-7a1437-1327104-16e2fe9d2406f6%22%2C%22%24device_id%22%3A%2216e2fe9d23f229-0410f1dfca8cbc-7a1437-1327104-16e2fe9d2406f6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; lianjia_ssid=3c189c63-a191-a6b8-d3ff-7c269dd93beb; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjRiMTlhMDQ1MDcwYzU5ZWRiYjQ0NmYxN2MyMTI3MDM3MWI5N2Q4YmM0YTVjNjU5ZmI2ODJhMjk1M2ZjZjgzMGM0MWRhOWZlZDJkOTliYzkwOTFhYTg5MzJmZjI4ZTJiOGFjZGUzZTYyYWMxYmU3MjAxMTZmMjc0NDUzZGVjZWMxNDcwYzcyY2Q5ODgzYTk3NWJjZDU0YjJiY2JlZTY5YmYyYmVmYWZiODlkN2I0YjYyM2U0MzYzZjA4ZjZiNDNiM2Q1NzlkNGRlYWJiYTg1Mjc5YTk4YmU4MGI0NzRhMTNjN2JhN2I0YzczYTFjYzQ1NjZjMjRlMDJlNDQ3MTQzZWJhZTE4ZjVkMGVkMjgzM2ZiMzQxYzVjZDcwYThlMGI3NTQ2OGNiYjMyOWNkNjAxMDM1YmNmNzkzMzA4YmE4ZWJkMGQwMjViNGMyNTdiYjEwNzgxYTAyM2Y0MDIzNjEwN1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyYTRkN2JmYlwifSIsInIiOiJodHRwczovL2NkLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
    "Host": "cd.lianjia.com",
    "Referer": "https://cd.lianjia.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent":random.choice(useragent) }
    # proxys = ["27.188.65.244:8060", "218.59.193.14:59941", "117.95.192.232:9999", "183.166.132.221:9999"]
    # try:
    #     # response = s.get(url, headers=headers, verify=False, proxies=random.choice(proxys))
    #     response = s.get(url, headers=headers, verify=False)
    # except:
    response = s.get(url=base_url, headers=headers, verify=False)
    # print(response.text)
    return response


def get_message(response):
    html=etree.HTML(response.text)
    info=[]
    divs=html.xpath("//div[@class='content__list']/div[@class='content__list--item']")
    for div in divs:
        house_name=div.xpath(".//a[@class='content__list--item--aside']/@title")[0].strip()
        address="".join(div.xpath(".//div[@class='content__list--item--main']/p[@class='content__list--item--des']//a//text()")).strip()
        area=div.xpath(".//div[@class='content__list--item--main']/p[@class='content__list--item--des']/text()[5]")[0].strip()
        price=div.xpath(".//span[@class='content__list--item-price']//text()")[0].strip()
        info.append([house_name,address,area,price])
    print(info)
    return info




# def next(next_url):
#     if len(next_url) !=0:
#         resp=s.get("https://cd.lianjia.com"+next_url)
#         get_message(resp)



        # // *[ @ id = "content"] / div[1] / div[1] / div[1] / div / p[2] / a[3]
        # return info


# def next_url(response):
#     html = etree.HTML(response.text)
#     info = []
#     # next_url=parse.urljoin(response.url,html.xpath("//a[@class='next']/@href]")[0])
#
#     print(next_url)
#     req=s.get(url=next_url)
#     get_message(req)
#     return html
def main():
    # response=get_url()
    # get_message(response)
    # next_url(response)
    i = 1
    while True:
        response = get_url(i)
        info= get_message(response)
        # req=get_parse(html)
        if i==100:
            break
        # get_parse(html)
        i = i + 1



if __name__ == '__main__':
    main()