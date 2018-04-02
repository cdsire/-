#coding:utf-8
from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '10254191'
API_KEY = 'eHP1Ku9GhxgvhElbXNEkufhU'
SECRET_KEY = 'pe0BHWBhEiPB5cBwgARmdaPS4EWN02N5'

aipImageClassify = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('4.jpg')

result=aipImageClassify.carDetect(image) #奔驰sls级
#result=aipImageClassify.animalDetect(image)
# result=aipImageClassify.plantDetect(image)  #非植物
print result
print result["result"][0]["name"]
