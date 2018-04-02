# -*- coding: utf-8 -*-
import scrapy
import lxml
import lxml.etree
import selenium
import selenium.webdriver
import time
from selenium.webdriver import ActionChains

import CTO51.items


class CtospiderSpider(scrapy.Spider):
    name = 'CTOspider'
    allowed_domains = ['edu.51cto.com']
    start_urls = ['http://edu.51cto.com/center/lec/index/list?edunav=&page=1']

    def __init__(self):
        super(CtospiderSpider, self).__init__()
        self.start_urls = self.geturllist(self.start_urls[0])

    # 获取51tco讲师的总页数
    # 抓取51tco的讲师总页面数量：
    #  由于跳转时弹出广告，影响数量的抓取，所以打开浏览器时需要手动关闭广告
    def geturllist(self, url):
        driver = selenium.webdriver.Chrome()  # 打开谷歌浏览器
        driver.get(url)  # 打开链接
        driver.implicitly_wait(5)  # 最多等待5秒
        data = driver.page_source.encode("utf-8").decode("utf-8")  # 获取页面资源
        endpage = driver.find_element_by_class_name("last")  # 获取页码的末页元素
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

    def parse(self, response):
        data = response.body
        mytree = lxml.etree.HTML(data)
        namelist = mytree.xpath("//ul[@class=\"Lecs\"]/li/div[2]/h2/a/text()")
        infolist = mytree.xpath("//ul[@class=\"Lecs\"]/li/div[2]/p[2]/text()")
        classlist = mytree.xpath("//ul[@class=\"Lecs\"]/li/div[2]/div[2]/p[1]/text()")
        peoplelist = mytree.xpath("//ul[@class=\"Lecs\"]/li/div[2]/div[2]/p[2]/text()")

        for i in range(len(namelist)):
            try:
                teacheritem = CTO51.items.Cto51Item()
                teacheritem["name"] = namelist[i]
                teacheritem["lessons"] = classlist[i]
                teacheritem["students"] = peoplelist[i]
                teacheritem["title"] = infolist[i]
                yield teacheritem
            except:
                print("error")
