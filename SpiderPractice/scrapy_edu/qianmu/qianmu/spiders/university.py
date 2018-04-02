# -*- coding: utf-8 -*-
import scrapy


class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['qianmu.iguye.com']
    start_urls = ['http://qianmu.iguye.com/2018USNEWS世界大学排名']

    def parse(self, response):
        links = response.xpath('//*[@id="content"]/table/tbody/tr/td[2]/a/@href').extract()
        for link in links:
            if not link.startswith('http://'):
                link = 'http://qianmu.iguye.com/%s' % link
            request = scrapy.Request(link, callback=self.parse_university)
            yield request

    def parse_university(self, response):
        table = response.xpath('//*[@id="wikiContent"]/div[1]/table/tbody')
        if not table:
            return
        table = table[0]
        keys = table.xpath('./tr/td[1]//text()').extract()
        cols = table.xpath('./tr/td[2]')
        values = [' '.join(col.xpath('.//text()').extract()) for col in cols]
        info = dict(zip(keys, values))
        yield info

