# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import os


class GeyanwangPipeline(object):

    def process_item(self, item, spider):
        return item


class GeyanwangSQLitePipeline():

    def __init__(self):
        self.setupDBCon()   # 连接数据库
        self.createTables() # 创建表


    def setupDBCon(self):
        self.con = sqlite3.connect(os.getcwd() + "/geyan.db")   # 创建数据库连接
        self.cur = self.con.cursor()    # 创建游标

    def createTables(self):
        self.dropGeyanTabler()  # 先删除表，再创建表，确保干净
        self.createGeyanTables()

    def createGeyanTables(self):
        sql = '''
            create table Geyan(
              id INTEGER PRIMARY KEY NOT NULL,
              content TEXT
            )
        '''
        self.cur.execute(sql)   # 执行

    def dropGeyanTabler(self):
        sql = '''
            drop table if exists Genyan
        '''
        self.cur.execute(sql)

    def closeDB(self):
        self.con.close()

    def process_item(self,item,spider):
        self.storeInDb(item)
        return item

    def storeInDb(self,item):
        print(item.get("content"))
        self.cur.execute("insert into Geyan(content) VALUES (?)",(item.get("content"),))
        self.con.commit()   # 提交

