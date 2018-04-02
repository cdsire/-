# -*- coding: utf-8 -*-
import multiprocessing
import multiprocessing.managers
import requests
import lxml
import lxml.etree
import re
import os
import Queue
import time


# 跟服务器一样，创建一个进程管理器，共享数据
class QueueManager(multiprocessing.managers.BaseManager):
    pass


# 输入一个url，返回一个数据集合
def download(url):
    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    mytable = myxml.xpath("//*[@cellpadding=\"0\"]//*[@cellpadding=\"1\"]")
    datalist = []
    for line in mytable:
        idlist = line.xpath("//td[1]/text()")
        typelist = line.xpath("//td[2]/a[1]/text()")
        titlelist = line.xpath("//td[2]/a[2]/text()")
        aboutlist = line.xpath("//td[2]/a[3]/text()")
        statuslist = line.xpath("//td[3]/span/text()")
        namelist = line.xpath("//td[4]/text()")
        datelist = line.xpath("//td[5]/text()")

        for i in range(len(typelist)):
            mygetstr = ""
            mygetstr += idlist[i + 1]
            mygetstr += "#"
            mygetstr += typelist[i]
            mygetstr += " # "
            mygetstr += titlelist[i]
            mygetstr += " # "
            mygetstr += aboutlist[i]
            mygetstr += " # "
            mygetstr += statuslist[i]
            mygetstr += " # "
            mygetstr += namelist[i + 1]
            mygetstr += " # "
            mygetstr += datelist[i + 1]
            mygetstr += "\r\n"  # 换行
            datalist.append(mygetstr)
    return datalist


if __name__ == '__main__':
    # 创建和服务器注册一样的两个获取任务和结果的函数
    QueueManager.register("get_task")
    QueueManager.register("get_result")
    manager = QueueManager(address=("169.254.212.217",8848),authkey="123456")
    # 连接服务器
    manager.connect()
    # 创建两个获取任务和结果的对象
    task = manager.get_task()
    result = manager.get_result()

    for i in range(1000):
        time.sleep(1)
        try:
            # 从服务端获取链接
            url = task.get()
            print "client get url:",url
            datalist = download(url)
            # 将得到的数据放入队列，等待服务端获取
            for line in datalist:
                result.put(line)
        except:
            pass
