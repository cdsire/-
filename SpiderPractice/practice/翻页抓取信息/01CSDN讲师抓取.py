# -*- coding: utf-8 -*-
import urllib.request
import urllib
import lxml
import lxml.etree
import re


# 抓取网页数据
def getpage(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

# 抓取所有的链接
def geturllist(url):
    urllist = []
    data = getpage(url)
    mytree = lxml.etree.HTML(data)  # 解析页面
    mytext = mytree.xpath("//*[@class=\"text\"][last()]/text()")[1]
    regex = re.compile("\d+",re.IGNORECASE) # 正则表达式提取
    num = eval(regex.findall(mytext)[0])
    print(num)

    pages = 0
    if num % 20 ==0:
        pages = num // 20
    else:
        pages = num //20 + 1

    for i in range(1,pages + 1):
        urllist.append("http://edu.csdn.net/lecturer?&page=" + str(i))

    return urllist

# 提取每页的页面数据
def getpagedata(url):
    data = getpage(url)
    mytree = lxml.etree.HTML(data)
    nodedata = mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/p/text()")
    nodename = mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/ul//li[1]/a/text()")
    nodelessions = mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/ul//li[2]/span/text()")
    nodestudents = mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/ul//li[3]/span/text()")

    for i in range(len(nodedata)):
        mystr = nodename[i] + " " + nodelessions[i] + " " + nodestudents[i] + " " + nodedata[i]
        mystr = mystr.replace("\n","")
        print(mystr)


starturl="http://edu.csdn.net/lecturer?&page=1"
mylist=geturllist(starturl)
for line in mylist:
    getpagedata(line)