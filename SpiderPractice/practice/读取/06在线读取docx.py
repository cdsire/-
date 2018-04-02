# -*- coding: utf-8 -*-
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup


url = "http://pythonscraping.com/pages/AWordDocument.docx"
wordfile = urlopen(url).read()
wordfile = BytesIO(wordfile)    # 转化为内存二进制
doc = ZipFile(wordfile)     # 把内存当作硬盘
xml_content = doc.read("word/document.xml") # 文档格式
print(xml_content)  # word本质就是xml
