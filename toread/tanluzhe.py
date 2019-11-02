import requests
from lxml import etree
import random


s = requests.session()


def get_urls():
    urls = []
    base_url = 'https://toread.tmall.com/i/asynSearch.htm?mid=w-18307703560-0&pageNo='
    for i in range(1, 3):
        urls.append(base_url + str(i))

    return urls

def get_page(url):
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
    headers = {
               "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "zh-CN,zh;q=0.9",
               "cookie": "cna=wHCoFc/vLCoCAXWw5B7DtxOA; sm4=620100; lid=%E6%88%8F%E5%AD%90%E7%8E%8B11; csa=0_0_0_0_0_0_0_0_0_0_0; hng=CN%7Czh-CN%7CCNY%7C156; pnm_cku822=; enc=T46KLrmXlYfhdjJ7QFLe%2BIhPqMkQd9tIHtzbuVJnWubMjSvKtEYHprDlKq1%2BLw5GNiakTp9oS2iRhNBT7GDFGA%3D%3D; t=bd2337eebef22c44b25a0e45f07218bd; tracknick=%5Cu620F%5Cu5B50%5Cu738B11; lgc=%5Cu620F%5Cu5B50%5Cu738B11; _tb_token_=fea17e808e373; cookie2=16dc5cb261439b80ad464ced3187bad3; tk_trace=1; _m_h5_tk=812244234df77bc9027055e859e4738d_1572677052846; _m_h5_tk_enc=8082fe6cad9145435e0910388a17e084; dnk=%5Cu620F%5Cu5B50%5Cu738B11; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&pas=0&cookie14=UoTbnx6XsacxKQ%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByua1K%2FWVp%2F3Aq5I%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&id2=UoH8WASXfFy2Hg%3D%3D&nk2=rL0IAjMyPBw%3D; uc4=id4=0%40UOnjmGG86l0kc2yVQLWps9t%2F4Way&nk4=0%40rpMZyHOyIvWOgrkjd3N3FtM3Tg%3D%3D; _l_g_=Ug%3D%3D; unb=1035543662; cookie1=UIHznojj%2BrCI65iyDW0DTo8QAbpSwFd4ACya5qhTzlU%3D; login=true; cookie17=UoH8WASXfFy2Hg%3D%3D; _nk_=%5Cu620F%5Cu5B50%5Cu738B11; sg=120; csg=4e6158a9; cq=ccp%3D0; l=dBTuJGPgqEUyoRqNBOCwourza77OSIRAguPzaNbMi_5aZ6Y1Bc_Okwsx4Fv6VjWfG0LB402lRpy9-etkiS-qlIaJhA3jlxDc.; isg=BObmTsiZh8wx0FP0rX1dF5r-N1yobwFEpnvEWNCP0InkU4ZtOFUpkIolqw_6eyKZ",
               "referer": "https://toread.tmall.com/search.htm?spm=a1z10.3-b-s.w4011-18307703560.417.64a9605f3doFEk&search=y&scene=taobao_shop&pageNo=1&tsearch=y",
               "user-agent": random.choice(useragent),
               "x-requested-with": "XMLHttpRequest"}
    # proxys = ["27.188.65.244:8060", "218.59.193.14:59941", "117.95.192.232:9999", "183.166.132.221:9999"]
    # try:
    #     # response = s.get(url, headers=headers, verify=False, proxies=random.choice(proxys))
    #     response = s.get(url, headers=headers, verify=False)
    # except:
    response = s.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        return response.text

    else:
        print("请求错误:{}".format(response.status_code))

def decide_if_loop(html):
    """通过解析要拿到的页面第一个数据，判断是否拿到真正的页面，如果假的页面，就返回False"""
    selector = etree.HTML(html)
    data = selector.xpath('/html/body/div/div[3]/div[1]/dl[1]/dd[2]/a/text()')[0]
    return False if not data else selector


def loop(url):

    html = get_page(url)
    selector = decide_if_loop(html)

    if not selector:
        loop(url)
    data = parse_detail(selector)
        # save_to_csv(data, filename)

def parse_detail(selector):
    """从拿到的真实页面中，解析出商品名，销量和价格"""

    data = []
    # 两个for循环解析一个html页面
    for i in range(1, 13):
        for j in range(1, 6):
            title = selector.xpath(
                '/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(j) + ']/dd[2]/a/text()')[0]
            price = selector.xpath('/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(
                j) + ']/dd[2]/div/div[1]/span[2]/text()')[0]
            num = selector.xpath('/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(
                j) + ']/dd[2]/div/div[3]/span/text()')[0]
            # 这个判断用于防止最后一页商品不全时，或者页面出现任何错误，值可能为空的情况
            if title and price and num:
                data.append([title.strip(), price.strip(), num.strip()])
    print(data)
    return data

def main():
    for url in get_urls():
        loop(url)


if __name__ == '__main__':
    main()