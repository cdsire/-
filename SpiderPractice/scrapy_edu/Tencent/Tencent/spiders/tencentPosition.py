# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


# 爬取腾讯社招网信息
class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'    # 爬虫名
    allowed_domains = ['tencent.com']   # 爬虫作用范围
    url = "https://hr.tencent.com/position.php?&start=" # 腾讯社招网首页
    offset = 0
    start_urls = [url + str(offset)]    # 每一页的地址集

    def parse(self, response):
        # 每页的十行循环抽取
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentItem()
            # 职位名称
            # '25663-金融云售中运维工程师（深圳/北京/上海）'
            try:
                item["positionname"] = each.xpath("./td[1]/a/text()").extract()[0]
                # 详情链接
                item["positionlink"] = each.xpath("./td[1]/a/@href").extract()[0]
                # 职位类别
                item["positiontype"] = each.xpath("./td[2]/text()").extract()[0]
                # 招聘人数
                item["peoplenum"] = each.xpath("./td[3]/text()").extract()[0]
                # 工作地点
                item["worklocation"] = each.xpath("./td[4]/text()").extract()[0]
                # 发布时间
                item["publishtime"] = each.xpath("./td[5]/text()").extract()[0]

                yield item
            except Exception as e:
                print("此处是空",e)
                pass

        if self.offset < 3500:
            self.offset += 10

        # 每次处理完一页的数据后，重新发送下一页面请求
        # self.offset自增10，同时拼接新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
