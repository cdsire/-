# -*- coding: utf-8 -*-
'''
参考文档：http://ai.baidu.com/docs#/OCR-Python-SDK/fa5138fd
AipOcr是OCR的Python SDK客户端，为使用OCR的开发人员提供了一系列的交互方法。
参考文档里面还有更多带参数的和其他的用法，由于经常更新，所以每次用的时候需要去更新需要的东西
'''
from aip import AipOcr


APP_ID = "10994778"
API_KEY = "ZzefGPsDT8YNbnPeyXeMIVik"
SECRET_KEY = "iMW2GVrlrPuTFuFuZtd7g7kBiCmZQvas"

# 读取图片
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

# 调用通用文字识别接口
aipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)
# 调用通用文字识别, 图片参数为本地图片
result = aipOcr.basicGeneral(get_file_content("chinese.jpg"))

for subdic in result["words_result"]:

    print subdic["words"]