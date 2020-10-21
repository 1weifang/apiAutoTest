#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@file:login.py
@time:2020/09/28
"""
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common.baseutil import BaseUtil
from interfaces.common.send_post_requests import SendPostRequests
from config.ipc.common.common_urls import LOGIN_URL


class Login(SendPostRequests):

    def __init__(self):
        super().__init__()
        self.base = BaseUtil()

    def get_login_url(self):
        '''
        定义登录的URL
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LOGIN_URL + "?&timeStamp=%s&lang=en" %(self.base.getTimeStamp())
        return url


    def get_login_data(self,email,password):
        '''
         定义邮箱密码登录的body
        :param email:
        :param password:
        :return:
        '''
        data = {
            "auth_type": "email_password",
            "auto": False,
            "client_id": "0778a347853545c08d496566e0d0180c",
            "client_secret": "a0b5ca0e003a398fc4793514b0b3f754",
            "device_name": "HUAWEI EVA-AL10",
            "email": email,
            "grant_type": "password",
            "imei": "a000006d937c5f",
            "password": self.base.MD5(password),
            "product_line_id": "4f975dc1a43d4117a6f3eb83b2cbc778",
            "scope": "all"
            }
        return data

if __name__ == '__main__':
    pass


