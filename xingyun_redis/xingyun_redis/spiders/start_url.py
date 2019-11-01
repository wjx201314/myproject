import  redis
conn=redis.Redis(host='localhost',port=6379)

class Rdis_url():
    def __init__(self):
        self.r=redis.Redis("localhost")
    def add_url(self,url):
        self.r.lpush("MovieSpider:start_urls",url)

r=Rdis_url()

for i in range(1,6):
    base_url='https://www.qichacha.com/gongsi_area.html?prov=SC&city=510100&p={}'.format(i)
    r.add_url(base_url)