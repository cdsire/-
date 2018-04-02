# -*- coding: utf-8 -*-
''' 这里用的是 : python3,pdfminer不在支持python3 '''
from urllib.request import urlopen
from io import StringIO
import csv


# 这里得到是二进制
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read()
data = data.decode("utf-8") # 解码
print(data)
# 这里用作数据分析，将数据放在内存中去分析
datafile = StringIO(data)   # 把内存当作磁盘
csvreader = csv.reader(datafile)
for line in csvreader:
    print(line)