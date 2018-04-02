# -*- coding: utf-8 -*-
import urllib2
import re
import threading
import Queue
import time


# 获取网页数据
def getdata(url):
    try:
        data = urllib2.urlopen(url).read().decode("utf-8")
        # 没有异常返回字符串
        return data
    except:
        # 有异常，返回空
        return ""

# 获取网页邮箱,data为网页数据
def getallemail(data):
    try:
        mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
        emaillist = mailregex.findall(data)
        return emaillist
    except:
        return []

# 获取网页所有的链接
def getallhttp(data):
    try:
        mailregex = re.compile(r"(http://\S*?)[\"|>|)]", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []

# 获取网页链接的主机域名
def gethostname(httpstr):
    try:
        hostregex = re.compile(r"(http://\S*?)/",re.IGNORECASE)
        # 正则提取出来的都是放在一个列表里面
        mylist = hostregex.findall(httpstr)
        if len(mylist) == 0:
            return None
        else:
            return mylist[0]
    except:
        return None

# 通过主机域名和页面内容中的href中的子链接拼接得到完整的url
def getabsurl(url,data):
    try:
        # 子链接url
        regex = re.compile("href=\"(.*?)\"",re.IGNORECASE)
        urllist = regex.findall(data)
        # 深拷贝，这样对拷贝文件操作时不会破坏原列表
        newurllist = urllist.copy()

        for data in newurllist:
            # 如果找到的href中的子链接有带http开头的，就移除掉
            if data.find("http://") != -1:
                urllist.remove(data)
            # 如果找到javascript文本页将其移除
            if data.find("javascript") != -1:
                urllist.remove(data)

        # 获取主机域名
        hostname = gethostname(url)
        # 如果主域名部位空
        if hostname != None:
            # 循环将主域名和子链接拼接，构成完整的url
            for i in range(len(urllist)):
                urllist[i] = hostname + urllist[i]

        return urllist
    except:
        return []

# 获取所有的url
def geteveryurl(data):
    alllist = []
    mylist1 = []
    mylist2 = []

    # 获取主域名
    mylist1 = getallhttp(data)
    # 如果域名不为空，通过主机域名获取完整的链接
    if len(mylist1) > 0:
        mylist2 = getabsurl(mylist1[0], data)

    alllist.extend(mylist1)
    alllist.extend(mylist2)
    return alllist

# 循环所有的url，获取邮箱和网页内容
def BFS(url, emailqueue):
    # 抓取页面信息
    pagedata = getdata(url)
    print "抓取", url
    # 获取页面邮箱
    emaillist = getallemail(pagedata)
    # 如果邮箱列表不为空
    if len(emaillist) != 0:
        for mail in emaillist:
            print mail
            # 将邮箱放入邮箱队列
            emailqueue.put(mail)

    urllist = geteveryurl(pagedata)
    if len(urllist) != 0:
        for myurl in urllist:
            # 限定线程数量
            with sem:
                threading.Thread(target=BFS, args=(url, emailqueue)).start()

# 保存邮箱
def savemail():
    global emailqueue
    mailfile = open("mail.txt","wb")
    while True:
        # 每过5秒保存一次邮箱
        time.sleep(5)
        while not emailqueue.empty():
            data = emailqueue.get()
            mailfile.write((data + "\r\n").encode("utf-8","ignore"))
            mailfile.flush()
    mailfile.close()

# 多线程提取所有url的邮箱
def BFSgo(url,emailqueue):
    global sem
    # 限定线程数量
    with sem:
        threading.Thread(target=BFS, args=(url, emailqueue))

# 邮箱队列
emailqueue = Queue.Queue()
# url队列
urlqueue = Queue.Queue()
# 控制最大线程100个
sem = threading.Semaphore(100)
# 5秒后开启一个线程savemail
timethread = threading.Timer(5,savemail)
timethread.start()


