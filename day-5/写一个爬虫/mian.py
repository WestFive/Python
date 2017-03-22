import requests
from bs4 import BeautifulSoup
import random
import urllib.request

def trage_spider(max_pages):
    page=1
    while page <= max_pages:
        page+=1
        url = 'https://www.youjizz.com/page/'+str(page)+'.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for img in soup.find_all('img',{'class':'lazy'}):
            #从soup对象中获取img 标签， class名叫 lazy
            images = img.get('data-original')
            #通常是src,但这里是data-original
            download_web_image(images)
            #下载的方法
            print(images)

def download_web_image(url):
    name = random.randrange(4,1000)
    full_name =str(name)+".jpg"
    print(full_name+"下载完成")
    urllib.request.urlretrieve(url,full_name)

#总共页码为一页
trage_spider(1)