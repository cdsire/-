# -*- coding: utf-8 -*-
import multiprocessing
import time
import os

from multiprocessing import Barrier


def getdata(data, myBarrier):
    with myBarrier:
        print os.getpid(), "start"
        time.sleep(3)
        print os.getpid(), "end", data * data


if __name__ == '__main__':
    # 足三而行
    myBarrier = multiprocessing.Barrier(3)
    mylist = [x for x in range(100)]
    processlist = []
    for data in mylist:
        process = multiprocessing.Process(target=getdata, args=(data, myBarrier))
        processlist.append(process)
        process.start()

    for process in processlist:
        process.join()

