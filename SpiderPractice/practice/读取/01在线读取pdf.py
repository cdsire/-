# -*- coding: utf-8 -*-
''' 这里用的是 : python3,pdfminer不在支持python3 '''
from pdfminer.layout import LAParams    # 布局段落
from pdfminer.converter import TextConverter    # 文本转换
from pdfminer.pdfinterp import PDFResourceManager   # 资源管理content
from pdfminer.pdfinterp import process_pdf
from io import StringIO
from io import open
from urllib.request import urlopen


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()  # 资源管理
    restr = StringIO()  # 分配内存，加载字符串
    laparams = LAParams()   # 段落
    device = TextConverter(rsrcmgr,restr,laparams=laparams) # 转换为文本
    process_pdf(rsrcmgr,device,pdfFile) # 抓取网页的文本
    device.close()  # 关闭设备

    content = restr.getvalue()  # 抓取字符串
    restr.close()   # 关闭
    return content


pdffile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
print(readPDF(pdffile)) # 读取pdf，当作文件
pdffile.close()


'''
在线读取pdf步骤：
    需要导入的模块（要使用process_pdf,需要在python3中安装pdfminer3k）：
    def readPDF(pdfFile):
        1.创建pdf资源管理器：
            rsrcmgr = PDFResourceManager()
        2.分配内存，加载字符串：
            restr = StringIO()
        3.处理段落问题：
            laparams = LAParams()
        4.创建转换为文本的驱动：
            device = TextConverter(rsrcmgr,restr,laparams=laparams) 
        5.抓取网页的文本：(这里的pdfFile指的是urlopen("pdf的网址"))
            process_pdf(rsrcmgr,device,pdfFile)
        6.关闭驱动：
            device.close()
        7.抓取字符串：
            content = restr.getvalue()
        8.关闭内存：
            restr.close()
        9.返回内容
            return content
    10.在主程序中打开网址：
        pdfFile = urlopen("pdf的网址")
    11.读取pdf，当作文件
        print(readPDF(pdfFile))
    12.关闭pdf文件：
        pdfFile.close()
'''


