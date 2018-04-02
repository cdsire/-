# -*- coding: utf-8 -*-
import multiprocessing
import requests
import lxml
import lxml.etree
import re
import os
import time


# 输入url，返回一个数据集合list
def download(url):

    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    mytable = myxml.xpath("//*[@cellpadding=\"0\"]//*[@cellpadding=\"1\"]")

    datalist = []
    # 循环表格，提取每个数据
    for line in mytable:
        idlist = line.xpath("//td[1]/text()")
        typelist = line.xpath("//td[2]/a[1]/text()")
        titlelist = line.xpath("//td[2]/a[2]/text()")
        aboutlist = line.xpath("//td[2]/a[3]/text()")
        statuslist = line.xpath("//td[3]/span/text()")
        namelist = line.xpath("//td[4]/text()")
        datelist = line.xpath("//td[5]/text()")

        for i in range(len(typelist)):
            # 创建空字符集，连接提取每个数据
            mygetstr = ""
            mygetstr += idlist[i + 1]
            mygetstr += " # "
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
            # 连接完每条数据，进行换行
            mygetstr += "\r\n"
            datalist.append(mygetstr)

    return datalist

# 获取所有行的数量
def geturlnumbers(url):
    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    # 获取分页列表
    mylist = myxml.xpath("//*[@class=\"pagination\"]/text()")
    # 提取数量文本
    text = mylist[len(mylist) - 1].strip()
    pat = re.compile("\d+",re.IGNORECASE)
    datalist = pat.findall(text)
    numbers = eval(datalist[0])
    return numbers

# 获取所有页面的url
def makeurllist(numbers):
    # 创建列表用来存放所有页面的url
    urllist = []
    if numbers % 30 ==0:
        for i in range(numbers // 30):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page=" + str(i))
    else:
        for i in range(numbers // 30 + 1):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page=" + str(i))
    return urllist

# 读取所有的数据压入到队列
def go(urllist,queue):
    # 循环每个页面
    for url in urllist:
        try:
            # 调用download函数获取所有文本
            linelist = download(url)
            for line in linelist:
                # 将所有的文本压入队列
                queue.put(line)
        except:
            print "error"
        else:
            # 提示这个网页被哪个进程抓取成功
            print os.getpid(),url
    print os.getpid(),"pushed data finish"

# 从队列中读取数据
def readdata(queue):
    file = open("multiprocessing.txt","wb")
    while not queue.empty():
        try:
            data = queue.get(timeout=15)
            print "get",data
            file.write(data.encode("utf-8",errors="ignore"))
            # 写入缓存，实时生效
            file.flush()
        except:
            pass
    file.close()


if __name__ == '__main__':

    numbers = geturlnumbers("http://wz.sun0769.com/index.php/question/questionType?type=4&page=30")
    urllist = makeurllist(numbers)
    plist = [[],[],[],[],[],[],[],[],[],[]]
    N = len(plist)
    print len(urllist)
    for i in range(len(urllist)):
        plist[i % N].append(urllist[i])

    queue = multiprocessing.Manager().Queue()
    processlist = []
    # 开启10条进程
    for urllist in plist:
        process = multiprocessing.Process(target=go,args=(urllist,queue))
        process.start()
        processlist.append(process)

    time.sleep(5)

    # 开条进程进行读取数据
    readprocess = multiprocessing.Process(target=readdata,args=(queue,))
    readprocess.start()
    processlist.append(readprocess)

    for p in processlist:
        # 等待所有进程退出
        p.join()
    print "okok"





