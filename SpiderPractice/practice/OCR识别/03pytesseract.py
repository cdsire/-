# -*- coding: utf-8 -*-
'''
1.PIL:python Imaging Library
    是python平台事实上的图像处理标准库，
2.如果安装了Anaconda,Pillow就已经可以用了
'''
import pytesseract
import pytesseract.pytesseract
import PIL
import PIL.Image


'''处理英文：
image = PIL.Image.open(r"E:\1703\data_analysis\day09\picture\english.jpg")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
print pytesseract.pytesseract.image_to_string(image)
'''

image = PIL.Image.open(r"E:\1703\data_analysis\day09\picture\chinese.jpg")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
print pytesseract.pytesseract.image_to_string(image,lang="chi_sim")

