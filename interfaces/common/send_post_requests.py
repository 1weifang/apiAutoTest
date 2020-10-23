#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:定义接口与统一的发送方法
@file:send_post_requests.py
@time:2020/10/20
"""
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import requests
import json
from loguru import logger

class SendPostRequests:

    def __init__(self):
        pass

    def send_post_requests(self,url,body):
        headers = {"Content-Type": "application/json"}
        logger.info("请求的URL为%s" %url)
        logger.info("请求的body为%s" %body)
        res = requests.post(url, data=json.dumps(body), headers=headers, timeout=30)
        if res.status_code == 200:
            logger.info("接口请求成功")
            logger.info("返回的response为%s" %res.json())
            return res.json()
        else:
            logger.error("接口请求失败！")
            logger.info("失败的原因为:%s" %res.json())


if __name__ == '__main__':
    pass