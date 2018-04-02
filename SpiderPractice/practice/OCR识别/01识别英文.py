# -*- coding: utf-8 -*-
'''
1.subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
2.subprocess.Popen（）中可以是一个字符串，也可以是一个list
3.OCR技术是光学字符识别的缩写(Optical Character Recognition)，
  是通过扫描等光学输入方式将各种票据、报刊、书籍、文稿及其它印刷品的文字转化为图像信息，
  再利用文字识别技术将图像信息转化为可以使用的计算机输入技术。
'''
import subprocess


p = subprocess.Popen([
    # tesseract用来图片文字OCR识别
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    # 文件路径
    r"E:\1703\data_analysis\day09\picture\english.jpg",
    "english"], # 这里的english代表输出英文
    stdout=subprocess.PIPE, # 通过管道输出
    stderr=subprocess.PIPE)

# 等待命令执行成功
p.wait()
# 输出文件存储
file= open("english.txt","r")
print file.read()