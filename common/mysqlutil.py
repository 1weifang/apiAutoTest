#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:58
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : mysqlUtils.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pymysql import connect,cursors
from pymysql.err import OperationalError
from builtins import int
from loguru import logger

class MysqlUtil:

    #构造函数
    def __init__(self,host,port,user,password,db):
        '''
        :param host:
        :param port:
        :param user:
        :param password:
        :param db:
        '''
        try:
            self.conn = connect(host=host,
                                port=int(port),
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )

        except OperationalError as e:
            print(e)

    def cursor(self):
        '''
        获得游标
        '''
        self.conn.cursor()

    def getDict(self):
        '''
        公共方法，获取id的字典
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("select *  from t_oc_tag_info ")
        Dict = cursor.fetchone()
        self.conn.commit()
        return Dict



    def test_tidb(self):
        '''
       测试方法
        :param taskName:
        :param startTime:
        :param endTime:
        :param exe_result:
        :return:
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM device_bind;")
        self.conn.commit()
        self.conn.close()


    def close(self):
        '''
        关闭mysql数据库
        '''

        self.conn.close()

    def test(self):
        logger.info("mysql测试")

if __name__ == "__main__":
    pass

















