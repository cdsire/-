# -*- coding: utf-8 -*-
import multiprocessing
import time
import os


def getdata(data):
    print os.getpid()
    time.sleep(3)
    print os.getpid()
    return data * data


if __name__ == '__main__':
    mylist = [x for x in range(100)]
    # 进程池，最大并发量为5
    pool = multiprocessing.Pool(processes=5)
    # 抓取进程池中的所有执行结果
    pool_outputs = pool.map(getdata, mylist)
    pool.join()
    pool.close()
    print pool_outputs
