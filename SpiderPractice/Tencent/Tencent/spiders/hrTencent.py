# -*- coding: utf-8 -*-
import scrapy
import Tencent.items


class HrtencentSpider(scrapy.Spider):
    name = 'hrTencent'
    offset = 0
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?amp;start=0&a=&start=#a0']

    def parse(self, response):
        for everydata in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            tencentitem = Tencent.items.TencentItem()
            tencentitem["name"] = everydata.xpath("./td[1]/a/text()").extract()
            tencentitem["detailLink"] = everydata.xpath("./td[1]/a/@href").extract()
            tencentitem["positionInfo"] = everydata.xpath("./td[2]/text()").extract()
            tencentitem["peopleNumber"] = everydata.xpath("./td[3]/text()").extract()
            tencentitem["workLocation"] = everydata.xpath("./td[4]/text()").extract()
            tencentitem["publishTime"] = everydata.xpath("./td[5]/text()").extract()
            yield tencentitem

        if self.offset < 200:
            self.offset += 10

        newurl = "http://hr.tencent.com/position.php?amp;start=0&a=&start="+str(self.offset)+"#a"
        yield scrapy.Request(newurl, self.parse)  # 翻页自己调用自己