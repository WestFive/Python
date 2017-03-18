import urllib2.request
import urllib2.error
response = urllib2.urlopen('http://www.baidu.com/')  
html = response.read()  
print (html)  
