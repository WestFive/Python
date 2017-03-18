import urllib.request  
import re  
import os  
foot='huaban001'  
url_re=re.compile(r'<img src="(http://img.hb.aicdn.com/.+?)"')  
url='http://huaban.com/favorite/beauty/'  
def url_open(url):  
    html=urllib.request.urlopen(url).read()  
    return html  
def get_img_adds(html):  
    img_addrs=url_re.findall(html)  
    img_addrs=list(set(img_addrs))  
    img_addrs.remove('http://img.hb.aicdn.com/23a58517fb73f86bca85937f069724486b3e00a44caa-GMc99I_sq75sf')  
    return img_addrs  
def save_img(img_addrs,filename=0):  
    for each in img_addrs:  
       with open(str(filename)+'.jpg','wb') as f:  
           filename+=1  
           img=url_open(each)  
           f.write(img)  
def download_huaban_img():  
 os.mkdir(foot)  
 os.chdir(foot)  
 html=url_open(url)  
 img_addrs=get_img_adds(html.decode('utf-8'))  
 save_img(img_addrs)  
if __name__=='__main__':  
    download_huaban_img()  