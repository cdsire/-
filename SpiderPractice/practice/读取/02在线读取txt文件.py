# -*- coding: utf-8 -*-
''' 这里用的是 : python3,pdfminer不在支持python3 '''
from urllib.request import urlopen


# print(type(urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt").read())) # <class 'bytes'>
print(urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt").read().decode("utf-8"))