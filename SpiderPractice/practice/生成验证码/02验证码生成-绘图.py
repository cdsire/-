# -*- coding: utf-8 -*-
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


image = PIL.Image.new(mode="RGB",
                           size=(220,230),
                           color=(255,255,255))

draw = PIL.ImageDraw.Draw(image,mode="RGB")
font = PIL.ImageFont.truetype("C:\Users\Administrator\SpiderPractice\practice\font\simfang.ttf",28)
draw.point([50,50],fill="yellow")
draw.point([5,80],fill="red")
draw.line((0,0,50,80),fill="red")
draw.arc((0,0,50,50),0,360,fill="black")
image.show()
with open("code2.png","wb") as file:
    image.save(file,format="png")