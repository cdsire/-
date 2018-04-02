# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings


class ScrapyBookPipeline(object):
    def process_item(self, item, spider):
        return item


class ScrapyBookMysqlPipeline(object):

    def __init__(self):
        settings = get_project_settings()
        self.database = settings["DATABASE"]
        self.connect()

    def connect(self):
        # 连接数据库
        self.conn = pymysql.connect(
            host=self.database["host"],
            port=self.database["port"],
            user=self.database["user"],
            password=self.database["password"],
            db=self.database["db"],
            charset=self.database["charset"]
        )
        # 获取游标
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        # name,author,info,img_url
        # sql = "insert into qf_book(name,author,info,img_url) values(%s,%s,%s,%s)" ,(item['name'],item['author'],item['info'],item['img_url'])
        sql = "insert into qf_book(book_name,author,info,img_url) values('%s','%s','%s','%s')"% (item.get("book_name"),item.get("author"),item.get("info"),item.get("img_url"))
        self.cursor.execute(sql)    # 执行sql语句
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()




'''
        settings = get_project_settings()
        self.database = settings["DATABASE"]
        self.connect()

    def connect(self):
        # 连接数据库
        self.conn = pymysql.connect(
            host=self.database["host"],
            port=self.database["port"],
            user=self.database["user"],
            password=self.database["password"],
            db=self.database["db"],
            charset=self.database["charset"]
        )
        # 获取游标
        self.cursor = self.conn.cursor()

'''

