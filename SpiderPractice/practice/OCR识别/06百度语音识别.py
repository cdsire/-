# -*- coding: utf-8 -*-
'''
语音识别 :将人类的语音中的词汇内容转换为计算机可读的输入，例如按键、二进制编码或者字符序列
'''
from aip import AipSpeech


APP_ID = "10994778"
API_KEY = "ZzefGPsDT8YNbnPeyXeMIVik"
SECRET_KEY = "iMW2GVrlrPuTFuFuZtd7g7kBiCmZQvas"


client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
# def asr(self, speech=None, format='pcm', rate=16000, options=None):
# 建立包含语音内容的Buffer对象, 语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写
# rate	int	采样率，16000，固定值
result = client.asr(get_file_content('auido.pcm'), 'pcm', 16000, {
    'dev_pid': '1536',
})
print result["result"][0]

# 从URL获取文件识别
# client.asr('', 'pcm', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
# })

