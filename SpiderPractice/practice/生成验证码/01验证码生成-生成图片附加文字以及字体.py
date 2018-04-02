# -*- coding: utf-8 -*-
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


# 设置底框
image = PIL.Image.new(mode="RGB",   # 颜色模式
                      size=(120,30),    # 大小
                      color=(10,70,90)) # 颜色配置

draw = PIL.ImageDraw.Draw(image,mode="RGB")
# 选择字体及大小
font = PIL.ImageFont.truetype(r"C:\Users\Administrator\SpiderPractice\practice\font\simfang.ttf",28)
draw.text([0,0],    # 坐标
          "micheal",   # 写入的文字
          "red",    # 字体颜色
          font=font)    # 字体

image.show()    # 显示查看

# 存储
with open("code.png","wb") as file:
    image.save(file,format="png")