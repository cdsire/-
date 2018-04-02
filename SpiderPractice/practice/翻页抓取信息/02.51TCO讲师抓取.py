import urllib.request
import urllib
import lxml
import lxml.etree
import re


def  getpage(url): #抓取网页数据
    return urllib.request.urlopen(url).read().decode("utf-8")

def geturllist(url):
    urllist=[]
    data=getpage(url)
    mytree = lxml.etree.HTML(data)  # 解析页面，
    mytext = mytree.xpath("//*[@class=\"fl\"][2]/text()")[3]# 抓取元素
    regex = re.compile("\d+", re.IGNORECASE)  # 正则表达式提取
    num = eval(regex.findall(mytext)[0])  # 整数类型，
    print(num)
    pages = 0
    if num % 20 == 0:
        pages = num // 20
    else:
        pages = num // 20 + 1
    for i in range(1, pages + 1):
        urllist.append("http://edu.51cto.com/center/lec/index/list?edunav=&page=" + str(i))
    return urllist

def  getpagedata(url):
    data = getpage(url)
    mytree = lxml.etree.HTML(data)  # 解析页面，
    nodelistinfo=mytree.xpath("//*[@class=\"Lecs\"]//li//div[2]//p/text()")
    nodelistname = mytree.xpath("//*[@class=\"Lecs\"]//li//div[2]/h2/a/text()")
    print(len(nodelistname),len(nodelistinfo))
    for  i  in range (len(nodelistname)):
        print(nodelistname[i],nodelistinfo[i*4],
                              nodelistinfo[i*4+1],
                              nodelistinfo[i*4+2],
                              nodelistinfo[i*4+3])

starturl="http://edu.51cto.com/center/lec/index/list?edunav=&page=1"
print( getpagedata(starturl))