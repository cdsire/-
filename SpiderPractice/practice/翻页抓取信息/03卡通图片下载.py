# -*- coding: utf-8 -*-
import urllib.request
import urllib
import lxml
import lxml.etree
import re
import selenium
import selenium.webdriver


# 模拟头部信息抓取网页数据
def getpage(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    # 模拟浏览器
    opener.addheaders = [headers]
    return opener.open(url).read().decode("utf-8")

# 抓取网页全部链接
def geturllist(url):
    urllist = []
    data = getpage(url)
    mytree = lxml.etree.HTML(data)
    mytext = mytree.xpath("//*[@class=\"view_bt\"]/h1/font//span[last()]/text()")
    num = eval(mytext[0])
    for i in range(1, num + 1):
        urllist.append("http://www.1kkk.com/ch21-462706-p"+str(i)+"/")
    return urllist

# selenium获取网页数据
def getpagedata(url):
    driver = selenium.webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(20)
    data = driver.page_source
    print(type(data))
    mytree = lxml.etree.HTML(data)  # 解析页面，
    print(data)
    srclist = mytree.xpath("//img[@id=\"cpimg\"]/@src")  # 抓取图片地址
    print(srclist)  # 列表
    urllib.request.urlretrieve(srclist[0], "pic/1.png")  # 保存

starturl = "http://www.1kkk.com/ch21-462706-p21/"
print(getpagedata(starturl))
