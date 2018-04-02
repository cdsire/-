# -*- coding: utf-8 -*-
import requests
import lxml
import lxml.etree
import re
from bs4 import BeautifulSoup


def  getpage(url):#提取页面数据
    response=requests.get(url)
    print(response.content.decode("utf-8"))

# 获取详情页的文章标题、内容
def  getpagedata(url):#提取页面数据
    response=requests.get(url)
    #print(response.content.decode("utf-8"))
    soup=BeautifulSoup(response.content.decode("utf-8"),"lxml")
    title=soup.find_all("h3",class_="j_chapterName")[0].string
    contentlist=soup.find_all("div",class_="read-content j_readContent")[0].find_all("p")
    content=""
    for line in contentlist:
        print(line.get_text())
        content+=line.get_text()
    return title,content

# 获取每个章节的链接、标题
def  getpagetilelist(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode("utf-8"), "lxml")
    titlelist=soup.find_all("li",attrs={"data-rid":re.compile("\d+",re.IGNORECASE)})
    for  line  in titlelist:
        linenovip=line.find_all("a",attrs={"href":re.compile("//read.*",re.IGNORECASE)})
        # print(linenovip)
        if len(linenovip)>0  and  linenovip!=None  and linenovip[0]!=None:
            print("http:"+linenovip[0]["href"])
            print( linenovip[0].get_text(), )



url="https://read.qidian.com/chapter/z2ltFfJvNR-3DdYzXPCGvA2/V6Uj_Hr6majgn4SMoDUcDQ2"
url="https://book.qidian.com/info/1009265821#Catalog"
getpagetilelist(url)