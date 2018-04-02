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

result = aipFace.match([
        get_file_content('huangjian.jpg'),
        get_file_content('face1.jpg'),
        get_file_content('face2.jpg'),
        get_file_content('face3.jpg'),
    ])
print result
