# -*- coding: utf-8 -*-
import random
import string
import sys
import math
from PIL import ImageFont,ImageDraw,ImageFilter, Image


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

# 验证码的文本
def make_text():
    source1 = string.digits    # 生成0-9之间的数字
    source2 = string.letters    # 生成所有的字母（包括大写和小写）
    source = []
    source.extend(source1)
    source.extend(source2)
    return "".join(random.sample(source,numbers))   # 随机选取四个

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

    image = image.transform((width + 30,height + 20),
                            Image.AFFINE,
                            (1,-0.5,0,-0.2,0.9,0),
                            Image.BILINEAR) # 扭曲

    # 处理边界
    # image = image.filter(ImageFilter.RankFilter)

    filename = u"C:\\Users\\Administrator\\SpiderPractice\\practice\\生成验证码\\code1" + "\\" + text + ".png"
    with open(filename,"wb") as file:
        image.save(file,format="png")

for i in range(100):
    bgfontrange()
    ftfontcolor()
    make_codepng()


'''
import string #导入string这个模块
print string.digits  #输出包含数字0~9的字符串
print string.letters  #包含所有字母(大写或小写)的字符串
print string.lowercase #包含所有小写字母的字符串
print string.uppercase  #包含所有大写字母的字符串
print string.punctuation #包含所有标点的字符串
print string.ascii_letters #与string.letters一样

print [chr(i) for i in range(65,91)]#所有大写字母
print [chr(i) for i in range(97,123)]#所有小写字母
print [chr(i) for i in range(48,58)]#所有数字
'''