# -*- coding: utf-8 -*-
'''
思路：
    1.这里使用进程分布式去爬取东莞阳光问政的页面信息
    2.这里要使用服务端和客户端的思路去写，一直的ip和端口去连接
    3.需要导入分布式进程管理器
    4.由服务端非配任务，客户端去执行，服务端只等待接受数据
    5.两边使用队列共享和传递信息
    这里：
        1.服务端爬取总信息量，由此利用总数和页面显示的信息数量，
          计算全部的url
          然后把客户端传过来的数据存储进文件
        2.客户端负责循环url去爬取页面信息
'''

import multiprocessing  # 分布式进程
import multiprocessing.managers # 分布式进程管理器
import time
import Queue
import requests
import re
import lxml
import lxml.etree


# 创建两个队列，用来传递任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()

# 创建两个函数，分别返回任务队列和结果队列
def return_task():
    return task_queue

def return_result():
    return result_queue


# 创建一个进程管理共享数据的类，继承于基本的进程管理器
class QueueManager(multiprocessing.managers.BaseManager):
    pass


# 提取所有页面总共的信息量
# 这里的url是随便哪个前面的页码，因为每个页面显示的总数都是一样的
def geturlnumbers(url):
    '''
    pagetext = requests.get(url).content --->   content返回str
    pagetext = requests.get(url).text  --->   text返回Unicode
    print type(pagetext)   --->使用此方法可以查看页面类型
    print chardet.detect(pagetext)  ---> 可以看到使用的编码'encoding': 'GB2312'
    然后获取网页时就知道用什么去解码
    print pagetext.decode("GB2312",errors="ignore")
    '''
    pagetext = requests.get(url).content
    myxml = lxml.etree.HTML(pagetext.decode("GB2312",errors="ignore"))
    # 抓取分页列表
    mylist = myxml.xpath("//*[@class=\"pagination\"]/text()")
    text= mylist[len(mylist) - 1].strip()
    pat = re.compile("\d+",re.IGNORECASE)
    datalist = pat.findall(text)
    numbers = eval(datalist[0])
    return numbers

def makeurllist(numbers):
    urllist = []
    if numbers % 30 == 0:
        for i in range(numbers // 30):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page="+str(i*30))
    else:
        for i in range(numbers // 30 + 1):
            urllist.append("http://wz.sun0769.com/index.php/question/questionType?type=4&page="+str(i*30))
    return urllist


if __name__ == '__main__':
    # 调用函数，得到总数和所有页url
    numbers = geturlnumbers("http://wz.sun0769.com/index.php/question/questionType?type=4&page=30")
    urllist = makeurllist(numbers)

    # 开启分布式支持
    multiprocessing.freeze_support()

    # 注册两个函数给客户端调用
    QueueManager.register("get_task",callable=return_task)
    QueueManager.register("get_result",callable=return_result)

    # 创建一个进程管理，共享数据的管理器
    # 传入ip/端口和密码
    manager = QueueManager(address=("169.254.212.217",8848),authkey="123456")
    # 开启管理器
    manager.start()

    # 获得的任务和结果
    task,result = manager.get_task(),manager.get_result()

    for url in urllist:
        # 将任务url放入队列,等待客户端获取
        task.put(url)
    print "server is waiting for......"

    # 指定存储的文件，一边读取，一边存储
    savefile = open("data.txt","wb")
    while True:
        # 从客户端获取数据
        res = result.get(timeout=1000)
        print "get data from client:",res
        savefile.write(res.encode("utf-8","ignore"))
        # 写入缓存，即时获取数据
        savefile.flush()

    savefile.close()
    manager.shutdown()  # 关闭服务器






