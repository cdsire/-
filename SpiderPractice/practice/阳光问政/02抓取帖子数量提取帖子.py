# -*- coding: utf-8 -*-
import requests
import chardet
import lxml
import lxml.etree
import re


# 抓取全部的网页链接
def geturlnumbers(url):

    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    mylist = myxml.xpath("//*[@class=\"pagination\"]/text()")
    text = mylist[len(mylist) - 1].strip()
    pat = re.compile("\d+",re.IGNORECASE)
    datalist = pat.findall(text)
    numbers = eval(datalist[0])
    return numbers

# 获取所有页面的url列表
def makeurllist(numbers):

    urllist = []
    if numbers % 30 == 0:
        for i in range(numbers // 30):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page="+str(i*30))
    else:
        for i in range(numbers // 30 + 1):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page="+str(i*30))
    return urllist


url = "http://wz.sun0769.com/index.php/question/questionType?type=4&page=300"
mylist = makeurllist(geturlnumbers(url))
for line in mylist:
    print line