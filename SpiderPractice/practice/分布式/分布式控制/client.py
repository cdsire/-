#coding:utf-8
import multiprocessing  #分布式进程
import multiprocessing.managers #分布式进程管理器
import random,time  #随机数，时间
import Queue #队列

class  QueueManger(multiprocessing.managers.BaseManager):#继承，进程管理共享数据
    pass

if __name__=="__main__":
    print "client add start "
    QueueManger.register("get_task")  # 注册函数调用服务器
    QueueManger.register("get_result")
    manger=QueueManger(address=("169.254.212.217",8868),authkey="123456")
    manger.connect()  #链接服务器
    task= manger.get_task()
    result =manger.get_result()  # 任务，结果

    for i  in range(1000):
        time.sleep(1)
        try:
            data=task.get()
            print "client get",data
            result.put( "client"+str(data+10))
        except:
            pass

