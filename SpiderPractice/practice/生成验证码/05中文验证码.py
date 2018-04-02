# -*- coding: utf-8 -*-
import random
import string
import sys
import math
from PIL import ImageFont, ImageDraw, ImageFilter, Image


# 字体路径
font_path = r"C:\Users\Administrator\SpiderPractice\practice\font\simfang.ttf"
# 位数
numbers = 4
# 验证码大小
size = (150,60)
# 背景颜色
bgcolor = (255,255,255)
# 字体颜色
fontcolor = (0,0,0)
# 干扰线/干扰线数量
draw_line = True
line_numbers = (1,5)

# 中文字符
class RandomChar():
    @staticmethod
    def Unicode():
        val = random.randint(0x4E00, 0x9FBF)    # 汉字的Unicode编码范围
        return unichr(val)

    @staticmethod
    def GB2312():
        head = random.randint(0xB0, 0xCF)  # 汉字的gb2312编码范围
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = (head << 8) | (body << 4) | tail
        str = "%x" % val
        return str.decode('hex').decode('gb2312',"ignore")

# 验证码的文本
def make_text():
    text = ""
    for i in range(4):
        text += RandomChar.GB2312()
    return text # ""中加上四个随机数

# 背景颜色
def bgfontrange():
    global bgcolor
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    bgcolor = (color1,color2,color3)

# 字体颜色
def ftfontcolor():
    global fontcolor
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    fontcolor = (color1, color2, color3)

# 生成干扰线
def make_line(draw,width,height):
    # 起始点坐标
    begin = (random.randint(0,width),random.randint(0,height))
    # 终点坐标
    end = (random.randint(0,width),random.randint(0,height))
    # 划线，规定线条颜色和线宽
    draw.line([begin,end],fill=fontcolor,width=3)

# 生成验证码
def make_codepng():
    # 图片的宽度和高度
    width,height = size
    # 创建图片
    image = Image.new("RGBA",(width,height),bgcolor)
    # 1.写入新创建的图片
    draw = ImageDraw.Draw(image)
    text = make_text()
    # 字体
    font = ImageFont.truetype(font_path,40)
    # 字体的宽高
    font_width,font_height = font.getsize(text)
    # 2.写入了文字
    draw.text(((width - font_width)/numbers,(height - font_height)/2),  # 宽高
              text, # 文本
              font=font,    # 字体
              fill=fontcolor)   # 填充颜色

    # 如果存在干扰线,打印make_line
    if draw_line:
        print "make_line"
        # 随机画出1-5个干扰线
        num = random.randint(1,6)
        for i in range(num):
            make_line(draw,width,height)

        # (1,-0.1,0,-0.2,0.9,0)
        num1 = random.uniform(0.9, 1)
        num2 = random.uniform(-0.3, 0)
        num3 = random.uniform(-0.1, 0.1)
        num4 = random.uniform(-0.3, 0.1)
        num5 = random.uniform(0.8, 1)
        num6 = random.uniform(0, 0.2)  # 生成小数，min,max
    image = image.transform((width + 30, height + 20),
                            Image.AFFINE,
                            (num1,num2,num3,num4,num5,num6),
                            Image.BILINEAR)  # 扭曲


    # 处理边界
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

    filename = u"C:\\Users\\Administrator\\SpiderPractice\\practice\\生成验证码\\ch_zn_verifier" + "\\" + text + ".png"
    with open(filename,"wb") as file:
        image.save(file,format="png")

for i in range(100):
    bgfontrange()
    ftfontcolor()
    make_codepng()

