# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from Pinduoduo.items import PinduoduoItem
import pymysql as pq


# from pymongo import MongoClient


class PinduoduoGoodsPipeline(object):
    """将商品详情保存到MongoDB"""

    def __init__(self):
        self.conn = pq.connect(host='10.1.10.109', user='datav', passwd='123456', db='pinduoduo', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sales = item.get("sales")
        price = item.get("price")
        normal_price = item.get("normal_price")
        goods_name = item.get("goods_name")
        goods_id = item.get("goods_id")

        if isinstance(item, PinduoduoItem):
            sql = "INSERT INTO pinduoduo(goods_id, goods_name, normal_price, price, sales) VALUES (%s, %s, %s, %s, %s)"
            self.cur.execute(sql, (goods_id, goods_name, normal_price, price, sales))
            self.conn.commit()
            return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


# CREATE TABLE `pinduoduo` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `goods_id` int(1),
#   `goods_name` varchar(255) DEFAULT NULL,
#   `normal_price` varchar(255) DEFAULT NULL,
#   `price` varchar(255) DEFAULT NULL,
#   `sales` int(11) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1409 DEFAULT CHARSET=utf8;