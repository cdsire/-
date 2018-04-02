# -*- coding: utf-8 -*-
import selenium
import selenium.webdriver
import time
import lxml
import lxml.etree
from selenium.webdriver import ActionChains
import urllib
import urllib.request


# 抓取51tco的讲师总页面数量：
#  由于跳转时弹出广告，影响数量的抓取，所以打开浏览器时需要手动关闭广告
'''
def getpagenumbers(url):
    driver = selenium.webdriver.Chrome()    # 打开谷歌浏览器
    driver.get(url)    # 打开链接
    driver.implicitly_wait(5)   # 最多等待5秒
    data = driver.page_source.encode("utf-8").decode("utf-8")   # 获取页面资源
    endpage = driver.find_element_by_class_name("last")    # 获取页码的末页元素
    print(endpage)
    print(type(endpage))

    ActionChains(driver).click(endpage).perform()  # 单机末页元素
    time.sleep(3)
    data2 = driver.page_source.encode("utf-8").decode("utf-8")  # 获取跳转页面的页面数据
    driver.implicitly_wait(5)   # 最多等待5秒
    mytree2 = lxml.etree.HTML(data2)    # 解析页面
    # 获取最后一个页面
    lastnumber = eval(mytree2.xpath("//ul[@class=\"pagination\"]/li[last()-2]/a/text()")[0])
    print(lastnumber)   # 打印结果总页
    time.sleep(10)
    driver.close()

getpagenumbers("http://edu.51cto.com/center/lec/index/list?edunav=&page=1")
'''

# response = urllib.request.urlopen("http://edu.51cto.com/center/lec/index/list?edunav=&page=1")
# data = response.read().decode("utf-8")
# print(data)

def geturllist(url):
    driver = selenium.webdriver.Chrome()  # 打开谷歌浏览器
    driver.get(url)  # 打开链接
    driver.implicitly_wait(5)  # 最多等待5秒
    data = driver.page_source.encode("utf-8").decode("utf-8")  # 获取页面资源
    endpage = driver.find_element_by_class_name("last")  # 获取页码的末页元素
    time.sleep(5)
    print(endpage)
    print(type(endpage))

    ActionChains(driver).click(endpage).perform()  # 单机末页元素
    time.sleep(3)
    data2 = driver.page_source.encode("utf-8").decode("utf-8")  # 获取跳转页面的页面数据
    driver.implicitly_wait(5)  # 最多等待5秒
    mytree2 = lxml.etree.HTML(data2)  # 解析页面
    # 获取最后一个页面
    lastnumber = eval(mytree2.xpath("//ul[@class=\"pagination\"]/li[last()-2]/a/text()")[0])

    urllist = []
    for i in range(1, lastnumber + 1):
        urllist.append("http://edu.51cto.com/center/lec/index/list?edunav=&page=" + str(i))
    return urllist

print(geturllist("http://edu.51cto.com/center/lec/index/list?edunav=&page=1"))