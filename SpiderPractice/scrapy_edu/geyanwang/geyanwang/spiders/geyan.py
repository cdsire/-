# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import codecs
from geyanwang.items import GeyanwangItem


class GeyanSpider(scrapy.Spider):
    name = 'geyan'
    allowed_domains = ['geyanw.com']
    start_urls = ['https://www.geyanw.com']

    def parse(self, response):
        # print(response.body)    # 测试环境是否正常，页面是否能正常获取
        # 从页面中抽取在items.py中定义的数据
        url = "https://www.geyanw.com/lizhimingyan/1834.html"
        # 发送请求
        yield Request(url=url,callback=self.get_content)

    def get_content(self,response):
        # 把响应的body保存在文件中
        encoding = response.encoding
        with codecs.open("geyan.html","w",encoding=encoding) as f:
            f.write(response.body.decode(encoding))

        # 找到当前页中的所有的数据
        datas = response.xpath('//div[@class="content"]/p').xpath("string(.)").extract()  # 根据xpath查找
        # datas = response.xpath('//div[@class="content"]/p/text()').extract()  # 根据xpath查找
        for data in datas:
            item = GeyanwangItem()
            # 过滤空行
            if not data.strip():
                continue
            item["content"] = data
            yield item



