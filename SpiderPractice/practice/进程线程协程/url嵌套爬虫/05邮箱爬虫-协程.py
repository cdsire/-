#coding:utf-8
import time
import os
import  urllib2
import re
import threading
import  Queue
import time
import gevent
import gevent.monkey
gevent.monkey.patch_all()#自动切换

def  geteveryurl(data):
    alllist=[]
    mylist1=[]
    mylist2=[]

    mylist1=getallhttp(data)
    if len(mylist1) >0:
        mylist2=getabsurl(  mylist1[0],data)

    alllist.extend(mylist1)
    alllist.extend(mylist2)
    return  alllist


#<a class="u-btn pre-btn" href="/m/post-140-393974-4.shtml"></a>
def  getabsurl(url,data):
    try:
        regex=re.compile("href=\"(.*?)\"",re.IGNORECASE)
        httplist=regex.findall(data)
        newhttplist=httplist.copy()#深拷贝
        for data  in  newhttplist:
            if  data.find("http://")!=-1:
                httplist.remove(data)
            if  data.find("javascript")!=-1:
                httplist.remove(data)
        hostname=gethostname(url)
        if hostname!=None:
            for  i  in range(len(httplist)):
                httplist[i]=hostname+httplist[i]

        return httplist
    except:
        return []


#http://bbs.tianya.cn/post-140-393974-1.shtml'
#http://bbs.tianya.cn
def  gethostname(httpstr):
    try:
        mailregex = re.compile(r"(http://\S*?)/", re.IGNORECASE)
        mylist = mailregex.findall(httpstr)
        if  len(mylist)==0:
            return None
        else:
            return mylist[0]
    except:
        return None


def  getallhttp(data):
    try:
        mailregex = re.compile(r"(http://\S*?)[\"|>|)]", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []


def  getallemail(data):
    try:
        mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []

def  getdata(url):
    try:
        data=urllib2.urlopen(url).read().decode("utf-8")
        return data  #没有异常返回字符串
    except:
        return "" #发生异常返回空

def  BFS(url):
    global emailqueue
    global urlqueue

    pagedata=getdata(url) #抓取页面数据
    print "抓取",url
    emailist=getallemail(pagedata)  #抓取页面的邮箱
    if len(emailist)!=0:
        for email  in emailist:
            print email
            emailqueue.put(email)

    urlist=geteveryurl(pagedata) #提取页面的链接，压入队列
    if len(urlist)!=0:
        for myurl in urlist:
            urlqueue.put(myurl)

def  savemail():#每过5秒，执行一次保存
    global  emailqueue
    mailfile=open("mail.txt","wb")
    i=0
    while True:
        i+=1
        time.sleep(5)
        while not  emailqueue.empty():
            data=emailqueue.get()
            mailfile.write(  (data+"\r\n").encode("utf-8","ignore") )
            mailfile.flush()
        yield i
    mailfile.close()

def  BFSgo(url):
    global emailqueue
    global urlqueue
    urlqueue.put(url)
    # 队列1个
    # 队列2000个
    savetool=savemail()
    while True:
        time.sleep(5)
        urllist = []
        for i in range(100):
            if not urlqueue.empty():
                urllist.append(urlqueue.get())  # 抓取一个url,压入队列
        tasklist = []
        for url in urllist: #根据urllist,新建一个协程组，自动切换
            tasklist.append(gevent.spawn(BFS,url))
        gevent.joinall(tasklist)
        next(savetool)#直接保存
        print "save"


emailqueue=Queue.Queue() #邮箱队列
urlqueue=Queue.Queue()#url队列
BFSgo("http://bbs.tianya.cn/m/post-140-393974-1.shtml")
