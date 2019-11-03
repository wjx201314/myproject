import requests
from lxml import etree
import random
import json
import urllib

s = requests.session()


def get_citys():
    citys = []
    base_url = 'https://www.huazhu.com/Basic/NativeCityOverView'
    useragent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
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
    headers = {
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "ASP.NET_SessionId=qajh5mxnw223dxmiafv1ylqb; t_s=baidupc; __utmc=107792157; gr_user_id=a6c017e9-dffd-4daa-9aa5-ceb0476e875b; showApp=false; _HZ_SessionId=ZJinsNycksPCOFsqySKR/sRwmH0A+rU0TqvlDdJdvHc=; __utma=107792157.309903369.1572708361.1572744499.1572746712.4; __utmz=107792157.1572746712.4.4.utmcsr=baidupc|utmccn=Baidu_CPC_M_huazhu|utmcmd=SEM|utmctr=huazhujiudian|utmcct=pinpai; gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd=01a1ea20-c4df-4a9b-9a58-78aeecf5966f; Hm_lvt_e5770a47472445b3f839a58a32b8abe5=1572708361,1572708376,1572746712; gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd_01a1ea20-c4df-4a9b-9a58-78aeecf5966f=true; __RequestVerificationToken=qviDcAsGJJwvvy3B8xr_c-NOkbEIllHteapINCJzkPz0LulYH9fA_yd0lHHzxCSDGciCmJMLip7Ga7vREn5Kl86JTIxAt90HGkuHXW7wCAZgzfJmn2AEjKMm1jfKEXnGl0Jdnp8P5T6FN-EfYKgBzA2; __utmb=107792157.6.9.1572747041613; Hm_lpvt_e5770a47472445b3f839a58a32b8abe5=1572747042",
                "Host": "www.huazhu.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent":random.choice(useragent) }
    response = s.get(base_url, headers=headers, verify=False)
    # print(type(response))
    jsondata=json.loads(response.text)
    dicts=jsondata["CityList"]
    citys=[]
    for dict in dicts:
        city=dict["CityID"]
        citys.append(city)
    print(citys)
    return citys

def get_page(i,citys):


    for city_id in citys:
        city_url="http://hotels.huazhu.com/?CityID="+city_id+"&CheckInDate=2019-11-03&CheckOutDate=2019-11-04&PageIndex="+i
        # headers={}
        data={"CityID": 1101}
        html=s.get(url=city_url,params=data)
        # print(html.text)
        return html

def get_parse(html):
    info = []
    rep=etree.HTML(html.text)
    pages=rep.xpath("//div[@class='hotellist_box Lvh']/div[@class='hotellist Lmt10']/div[@class='hotel']")

    for page in pages:
        hotel_name=page.xpath(".//h2/text()")[0].strip()
        address=page.xpath(".//div[@class='address']/text()")[0].strip()
        # price=page.xpath(".//div[@class='hotelname  ']/a/@title")[0]
        rate=page.xpath(".//div[@class='score Ltar']/span[@class='Ldib Lpl5']/text()")[0].strip()
        info.append([hotel_name,address,rate])
    print(info)
    return info



# def next_url():

# def decide_if_loop(html):
#     """通过解析要拿到的页面第一个数据，判断是否拿到真正的页面，如果假的页面，就返回False"""
#     selector = etree.HTML(html)
#     data = selector.xpath('/html/body/div/div[3]/div[1]/dl[1]/dd[2]/a/text()')[0]
#     return False if not data else selector
# # #
# #
# # def loop(url):
# #
# #     html = get_page(url)
# #     selector = decide_if_loop(html)
# #
# #     if not selector:
# #         loop(url)
# #     data = parse_detail(selector)
# #         # save_to_csv(data, filename)
# #
# # def parse_detail(selector):
# #     """从拿到的真实页面中，解析出商品名，销量和价格"""
# #
#     data = []
#     # 两个for循环解析一个html页面
#     for i in range(1, 13):
#         for j in range(1, 6):
#             title = selector.xpath(
#                 '/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(j) + ']/dd[2]/a/text()')[0]
#             price = selector.xpath('/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(
#                 j) + ']/dd[2]/div/div[1]/span[2]/text()')[0]
#             num = selector.xpath('/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(
#                 j) + ']/dd[2]/div/div[3]/span/text()')[0]
#             # 这个判断用于防止最后一页商品不全时，或者页面出现任何错误，值可能为空的情况
#             if title and price and num:
#                 data.append([title.strip(), price.strip(), num.strip()])
#     print(data)
#     return data

def main():
    # citys=get_citys()
    i=1
    citys=get_citys()
    while True:
        html=get_page(str(i),citys)
        # req=get_parse(html)
        if len(get_parse(html))==0:
            break
        # get_parse(html)
        i=i+1
    # get_city(response)

if __name__ == '__main__':
    main()