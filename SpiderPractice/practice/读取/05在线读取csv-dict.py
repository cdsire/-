# -*- coding: utf-8 -*-
''' 这里用的是 : python3,pdfminer不在支持python3 '''
from urllib.request import urlopen
from io import StringIO
import csv


data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read()
data = data.decode("ascii") # 解码
datafile = StringIO(data)   # 内存当作磁盘，用来做网页数据分析
dictreader = csv.DictReader(datafile)   # 字典读取
print(dictreader.fieldnames)    # 字段：['Name', 'Year']

for line in dictreader:
    print(line)


'''
print(type(data))   # <class 'bytes'>

print(type(data))   # <class 'str'>

print(datafile) # <_io.StringIO object at 0x000001C64BD561F8>

print(dictreader)   # <csv.DictReader object at 0x000001D9DD40B198>
'''
