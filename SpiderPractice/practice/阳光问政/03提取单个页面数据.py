# -*- coding: utf-8 -*-
import requests
import chardet
import lxml
import lxml.etree
import re


def getdataformurl(url):
    '''这里的数据表格多层嵌套，所以常规的xpath提取方法不能提取'''
    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    # 这里提取的只是一个表格，不是数据
    mytable = myxml.xpath("//*[@cellpadding=\"0\"]//*[@cellpadding=\"1\"]")
    idlist = []
    typelist = []
    titlelist = []
    aboutlist = []
    statuslist = []
    namelist = []
    datelist = []
    for line in mytable:
        idlist = line.xpath("//td[1]/text()")
        typelist = line.xpath("//td[2]/a[1]/text()")
        titlelist = line.xpath("//td[2]/a[2]/text()")
        aboutlist = line.xpath("//td[2]/a[3]/text()")
        statuslist = line.xpath("//td[3]/span/text()")
        namelist = line.xpath("//td[4]/text()")
        datelist = line.xpath("//td[5]/text()")
        print len(idlist), len(typelist), len(titlelist), len(aboutlist), len(statuslist), len(namelist), len(datelist)
        print idlist
        print namelist
        print datelist
        for i in range(len(typelist)):
            print idlist[i + 1], typelist[i], titlelist[i], aboutlist[i], statuslist[i], namelist[i + 1], datelist[i + 1]


getdataformurl("http://wz.sun0769.com/index.php/question/questionType?type=4&page=81240")