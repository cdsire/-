# -*- coding: utf-8 -*-
''' 这里用的是 : python3,pdfminer不在支持python3 '''
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
# 解析页面
bsobj = BeautifulSoup(html,"html.parser")
content = bsobj.find("div",{"id":"mw-content-text"}).get_text() # python3默认utf-8格式
print(type(content))    # <class 'str'>
print(type(content.encode("utf-8")))    # <class 'bytes'>
print(type(content.encode("utf-8").decode("utf-8")))    # <class 'str'>
print(content)


'''
1. python3默认utf-8编码格式
2. str格式用utf-8编码会转化成bytes二进制
3. bytes用utf-8会转化成str字符串
'''