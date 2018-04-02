# -*- coding: utf-8 -*-
'''
参考文档：http://ai.baidu.com/docs#/OCR-Python-SDK/fa5138fd
AipOcr是OCR的Python SDK客户端，为使用OCR的开发人员提供了一系列的交互方法。
参考文档里面还有更多带参数的和其他的用法，由于经常更新，所以每次用的时候需要去更新需要的东西
'''
from aip import AipSpeech

import time
import pygame
import mp3play


APP_ID = "10994778"
API_KEY = "ZzefGPsDT8YNbnPeyXeMIVik"
SECRET_KEY = "iMW2GVrlrPuTFuFuZtd7g7kBiCmZQvas"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# synthesis(self, text, lang='zh', ctp=1, options=None)
# zh : 语言填写，用“zh”，必须填写
# ctp : 客户端类型选择，web端填写1，必须填写
# vol : 音量，取值0-15，默认为5中音量，非必须参数，通常写在字典中
# spd : 语速，取值0-9，默认为5中语速
# per : 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
result  = client.synthesis('你好百度，你好百度，你好百度', 'zh', 1, {
    'vol': 5,'spd':8,'per':4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)


# filename = "auido.mp3"
# pygame.mixer.init() # 初始化，mixer会有混合音
# pygame.mixer.music.load(filename)
# pygame.mixer.music.play()
# time.sleep(10)

# 使用mp3play播放器就不需要打开原文件去播放了
filename = "auido.mp3"
player = mp3play.load(filename)
player.play()
time.sleep(10)


