#-*-coding:utf-8-*-

import re
import urllib
import urllib2

#page = 1
url = 'http://www.qiushibaike.com/textnew/'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<h2>(.*?)<.*?content">(.*?)<.*?number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print '----------------------'
        print item[0],item[1],item[2]
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
