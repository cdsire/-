# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.linkextractors import LinkExtractor # 提取超链接
from scrapy.spiders import CrawlSpider, Rule   # 提取超链接的规则

import tianya_email.items


class TianyaSpider(CrawlSpider):
    name = 'tianya'
    allowed_domains = ['tianya.cn']
    start_urls = ['http://bbs.tianya.cn/post-140-393977-1.shtml']

    # response提取超链接
    pagelinks = LinkExtractor(allow=(""))
    # 根据规则提取的链接，用一个函数处理，follow是一直循环下去,返回的urllist
    rules = [Rule(pagelinks, callback="parse_mail", follow=True)]

    # def __init__(self):
    #     super().__init__(self)
    #     scrapy.Request("http://bbs.tianya.cn/post-140-393977-1.shtml",
    #                    callback="parse_mail",
    #                    dont_filter=True)    # 爬取当前页面


    def parse_mail(self, response):
        savefile = open("tianya.html", "w")
        pagedata = response.body.decode("gbk", "ignore")
        savefile.write(pagedata)
        savefile.close()

        regex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
        maillist = regex.findall(pagedata)

        for mail in maillist:
            myitem = tianya_email.items.TianyaEmailItem()
            myitem["email"] = mail
            myitem["url"] = "http://bbs.tianya.cn/post-140-393977-1.shtml"
            yield myitem

