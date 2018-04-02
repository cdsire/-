# -*- coding: utf-8 -*-
import requests
import chardet



def geturl(url):
    ''' text返回Unicode  content返回str '''
    pagetext = requests.get(url).content
    # pagetext = requests.get(url).text
    print type(pagetext)    # <type 'str'>
    print chardet.detect(pagetext)  # 'encoding': 'GB2312'
    # 获取网页
    # print pagetext.decode("GB2312",errors="ignore")

geturl("http://wz.sun0769.com/index.php/question/questionType?type=4&page=300")


'''
             编码:         类型:       encode之后类型:      decode之后类型:
"a"          #ascii,       str            str               unicode
"中国"       #utf-8        str          不可编码              unicode
u"中国"      #utf-8       unicode       不可以编码            不可以解码

'''