#-*-coding:utf-8-*-

import re
import urllib
import urllib2
import thread
import time

#page = 1
class QB:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'mozilla/5.0 (x11; ubuntu; linux i686; rv:39.0) gecko/20100101 firefox/39.0'
        self.headers = {'user-agent':self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            if self.pageIndex == 1:
                url = 'http://www.qiushibaike.com/textnew/'
            else:
                url = 'http://www.qiushibaike.com/textnew/page/'+str(pageIndex)
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return none
        pattern = re.compile('<h2>(.*?)<.*?content">(.*?)<.*?number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            replaceBR = re.compile('</br>')
            text = re.sub(replaceBR,"\n",item[1])
            pageStories.append([item[0].strip(),text.strip(),item[2].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            pageStories = self.getPageItems(self.pageIndex)
            if pageStories:
                self.stories.append(pageStories)
                self.pageIndex += 1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input =="Q":
                self.enable = False
                return
            print u"第%d页\t作者:%s\t赞:%s\n%s"%(page,story[0],story[2],story[1])

    def start(self):
        print u"正在读取糗事百科，请回车查看新段子，Q推出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QB()
spider.start()


