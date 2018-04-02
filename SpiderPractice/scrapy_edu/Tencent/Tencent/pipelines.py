# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3
import os

'''
# 功能：保存item数据
class TencentPipeline(object):

    def __init__(self):
        # 保存到tencent.json文件中
        self.filename = open("tencent.json","w")

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        print(type(text))
        self.filename.write(str(text.encode("utf-8")))
        return item

    def close_spider(self,spider):
        self.filename.close()
'''

class TencentPipeline(object):

    def process_item(self,item,spider):
        return item

class TencentSQLitePipeline():

    # 连接数据库，创建表
    def __init__(self):
        self.setupDBCon()
        self.createTables()

    # 创建数据库，并建立游标
    def setupDBCon(self):
        self.con = sqlite3.connect(os.getcwd() + "/tencent.db")
        self.cur = self.con.cursor()

    # 创建表
    def createTables(self):
        self.dropTencentTable()
        self.createTencentTable()

    def createTencentTable(self):
        sql = '''
            create table Tencent(
                id integer primary key not NULL,
                positionname varchar(100),
                positionlink varchar(80),
                positiontype varchar(30),
                peoplenum varchar(10),
                worklocation varchar(10),
                publishtime date)
        '''
        self.cur.execute(sql)

    def dropTencentTable(self):
        sql = '''
            drop table if exists Tencent
        '''
        self.cur.execute(sql)

    def closeDB(self):
        self.con.close()

    def process_item(self,item,spider):
        self.storeInDB(item)
        return item

    def storeInDB(self,item):
        self.cur.execute(
            "insert into Tencent(positionname,positionlink,positiontype,peoplenum,worklocation,publishtime) values (?,?,?,?,?,?)",
            (item.get("positionname"),item.get("positionlink"),item.get("positiontype"),item.get("peoplenum"),item.get("worklocation"),item.get("publishtime"))
        )
        self.con.commit()



