# -*- coding: utf-8 -*-
from aip import AipFace


APP_ID = "10994778"
API_KEY = "ZzefGPsDT8YNbnPeyXeMIVik"
SECRET_KEY = "iMW2GVrlrPuTFuFuZtd7g7kBiCmZQvas"

aipFace = AipFace(APP_ID,API_KEY,SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

# 调用人脸属性检测接口
# result = aipFace.detect(get_file_content('face.jpg'))
# print result

# 定义参数变量
options = {
    'max_face_num':1,   # 最多人脸数
    'face_fields':'age,beauty,expression,faceshape'
}

# 调用人脸属性识别接口
result = aipFace.detect(get_file_content('wuyanzu.bmp'),options)
print result


