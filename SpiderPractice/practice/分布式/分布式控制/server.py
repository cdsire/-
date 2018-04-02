#coding:utf-8
import multiprocessing  #分布式进程
import multiprocessing.managers #分布式进程管理器
import random,time  #随机数，时间
import Queue #队列
# import os
task_queue=Queue.Queue() #任务
result_queue=Queue.Queue() #结果

def  return_task(): #返回任务队列
    return task_queue

def return_result(): #返回结果队列
    return   result_queue

class  QueueManger(multiprocessing.managers.BaseManager):#继承，进程管理共享数据
    pass

if __name__=="__main__":
    # os.system("calc")
    multiprocessing.freeze_support()#开启分布式支持
    QueueManger.register("get_task",callable=return_task)#注册函数给客户端调用
    QueueManger.register("get_result", callable=return_result)
    manger=QueueManger(address=("169.254.212.217",8868),authkey="123456") #创建一个管理器，设置地址与密码
    manger.start() #开启
    task,result=manger.get_task(),manger.get_result() #任务，结果
    for  i  in range(10000):
        print ('task add data',i)
        task.put(i)
    print ("waitting for------")
    savefile=open("add.txt","wb") #结果写入文本
    for  i  in range(10000):
        res=result.get(timeout=100)
        print ("get data",res)
        savefile.write(res)
        savefile.flush()
    savefile.close()
    manger.shutdown()#关闭服务器

