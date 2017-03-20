import random
import urllib.request

def download_web_image(url):
    name = random.randrange(4,1000)
    full_name =str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image('https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2607444671,3720724254&fm=21&gp=0.jpg')

