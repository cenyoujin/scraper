#-*-coding:utf-8-*-
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({

})
loginUrl = ''

