# -*- coding: utf-8 -*-
import urllib.request
import urllib

from bs4 import BeautifulSoup


def  getpage(url): #抓取网页数据
    return urllib.request.urlopen(url).read().decode("utf-8")

# 获取链接
def geturllist(url):
    urllist = []
    data = getpage(url)
    soup = BeautifulSoup(data, "lxml")
    numbers = eval(soup.find_all("p", class_="pg")[0].find("strong").string)
    pages = numbers
    for i in range(1,pages + 1):
        urllist.append("http://kaijiang.zhcw.com/zhcw/html/ssq/list_" + str(i)+".html")
    return urllist

# 获取网页数据
def getpagedata(url):
    data = getpage(url)
    soup = BeautifulSoup(data, "lxml")
    tags = soup.find_all("tr")  # 每一行
    print(len(tags))
    # 去掉前两个和最后一个
    for i in range(2, len(tags) - 1):
        tag = tags[i]
        tds = tag.find_all("td")
        td4 = tds[4].find("strong")
        ems = tag.find_all("td")[2].find_all("em")  # 摸奖号码
        mystr = tds[0].get_text() + "  " + tds[1].get_text() + "  " + ems[0].get_text()+" "+ems[1].get_text() + " " + ems[2].get_text() \
                + " " + ems[3].get_text()+ " " + ems[4].get_text() + " " + ems[5].get_text() + " " + ems[6].get_text() + "  " \
                + tds[3].string + "  " + td4.get_text() + "  " + tds[5].string
        mystr = mystr.replace("\r\n", "")
        print(mystr)



url="http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"
print(getpagedata(url))



