# -*- coding: utf-8 -*-
import subprocess


p = subprocess.Popen([
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    r"E:\1703\data_analysis\day09\picture\chinese.jpg",
    "chinese",
    "-l",   # language
    "chi_sim"], # 简体中文的意思
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)

p.wait()    # 等待命令执行成功
file = open("chinese.txt","r")
print file.read()
