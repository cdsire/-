# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor # LinkExtractor是一个专门用来抽取Link的库
from scrapy.spiders import Rule,CrawlSpider # crawlspider是Spider的子类,它可以定义规则，根据规则抽取链接
from scrapy_book.items import ScrapyBookItem
import codecs   # 专门用作编码转换


class DushuSpider(CrawlSpider):
    name = 'dushu'
    allowed_domains = ['dushu.com']
    start_urls = ['https://www.dushu.com/book/1158.html']

    rules = (
        Rule(LinkExtractor(allow=r"/book/1158_\d+\.html"),callback="parse_book"),
    )
    count = 1
    # 方法名不能为parse，会覆盖CrawlSpider中的同名方法
    def parse_book(self, response):
        encoding = response.encoding
        self.count +=1
        with codecs.open("book_list_{page}.html".format(page=self.count),"w",encoding=encoding) as f:
            f.write(response.body.decode(encoding))
        book_list = response.xpath("//div[@class=\"bookslist\"]/ul/li")

        try:
            for book in book_list:
                item = ScrapyBookItem()
                item["book_name"] = book.xpath(".//h3/a/text()").extract()[0]
                item["author"] = book.xpath(".//p[1]").xpath("string(.)").extract()[0]
                item["info"] = book.xpath(".//p[2]/text()").extract()[0]
                item["img_url"] = book.xpath(".//div[@class=\"img152 float-left margin-right\"]/a/img/@src").extract()[0]
                yield item
        except Exception as e:
            print(e)

