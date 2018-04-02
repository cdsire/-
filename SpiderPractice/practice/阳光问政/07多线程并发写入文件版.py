# -*- coding: utf-8 -*-
import requests
import lxml
import lxml.etree
import re
import threading


# 获取全部帖子数量，用来计算页数
def geturlnumbers(url):

    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    mylist = myxml.xpath("//*[@class=\"pagination\"]/text()")
    text = mylist[len(mylist) - 1].strip()
    pat = re.compile("\d+",re.IGNORECASE)
    datalist = pat.findall(text)
    numbers = eval(datalist[0])
    return numbers

# 获取全部的网页url
def makeurllist(numbers):

    urllist = []
    if numbers % 30 == 0:
        for i in range(numbers // 30):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page=" + str(i))
    else:
        for i in range(numbers // 30 + 1):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page=" + str(i))
    return urllist

# 提取页面内容，存入文件
def download(urllist,file):
    for url in urllist:
        try:
            pagetext = requests.get(url).content
            myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
            # 这里得到的是一个嵌套的表格，不是列表
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

                mygetstr = ""
                for i in range(len(typelist)):
                    print idlist[i + 1],typelist[i], titlelist[i], aboutlist[i], statuslist[i], namelist[i + 1], datelist[i + 1]
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
                    mygetstr += "\r\n"  # 换行
                    with rlock:
                        file.write(mygetstr.decode("utf-8",errors="ignore"))
        except:
            print "error"

# 避免线程冲突
rlock = threading.RLock()
numbers = geturlnumbers("http://wz.sun0769.com/index.php/question/questionType?type=4&page=81240")
urllist = makeurllist(numbers)
file = open("morethreading.txt","wb")
clist = [[],[],[],[],[],[],[],[],[],[]]
N = len(clist)
# 循环所有页
for i in range(len(urllist)):
    # 将所有页分别加入到10个线程里面
    clist[i % N].append(urllist[i])

threadlist = []
# 开启10条线程
for i in range(N):
    mythread = threading.Thread(target=download,args=(urllist,file))
    mythread.start()
    threadlist.append(mythread) # 加入线程列表

for t in threadlist:
    t.join()    # 阻塞等待每条线程都跑完

file.close()