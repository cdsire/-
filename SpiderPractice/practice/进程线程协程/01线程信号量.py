# -*- coding: utf-8 -*-
import threading
import time


def myThread(name):
    with sep:
        for i in range(10):
            time.sleep(1)
            print name, str(i), threading.current_thread().name

# 控制最大并发量
sep = threading.Semaphore(3)

threadlist = []
for name in ['a','b','c','d','e']:
    mythd = threading.Thread(target=myThread, args=(name,))
    mythd.start()
    # 循环加入到列表
    threadlist.append(mythd)

for thread in threadlist:
    thread.join()
