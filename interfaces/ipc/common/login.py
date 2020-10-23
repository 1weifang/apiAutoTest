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
from config.ipc.common.common_urls import *


class Login(SendPostRequests):

    def __init__(self):
        super().__init__()
        self.base = BaseUtil()

    def get_mi_login_url(self,mi_base_url):
        '''
        定义mi登录的URL
        :return:
        '''
        url = mi_base_url + LOGIN_URL + "?&timeStamp=%s&lang=en" %(self.base.getTimeStamp())
        return url


    def get_mi_login_Android_email_password_data(self,email,password):
        '''
         定义mi安卓邮箱密码登录的body
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

    def get_mi_refresh_token_url(self,mi_base_url):
        '''
        定义mi刷新token的URL
        :return:
        '''
        url = mi_base_url + REFRESH_TOKEN_URL + "?&timeStamp=%s&lang=en" %(self.base.getTimeStamp())
        return url


    def get_mi_refresh_token_data(self,refresh_token):
        '''
         定义mi安卓刷新token的body
        :param access_token:
        :return:
        '''
        data = {
                "client_id": "0778a347853545c08d496566e0d0180c",
                "client_secret": "a0b5ca0e003a398fc4793514b0b3f754",
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "scope": "all"
                }
        return data

    def get_mi_login_auth_data(self):
        '''
         定义mi安卓鉴权登录的body
        :return:
        '''
        data = {
            "client_id": "0778a347853545c08d496566e0d0180c",
            "client_secret": "a0b5ca0e003a398fc4793514b0b3f754",
            "grant_type": "client_credentials",
            "scope": "all"
            }
        return data


    def get_iot_login_url(self,iot_base_url):
        '''
        定义iot登录的URL
        :return:
        '''
        url = iot_base_url + LOGIN_URL + "?&timeStamp=%s&lang=en" %(self.base.getTimeStamp())
        return url


    def get_iot_login_data(self,station):
        '''
         定义iot的body
        :param station:
        :return:
        '''
        data = {
                "client_id": "9c33e08830c243c597246c71e3c2f458",
                "client_secret": "237e61fdc48a46908736c499685e9f34",
                "scope": "all",
                "grant_type": "password",
                "sn": station,
                "auth_type": "sn_password"
                }
        return data



if __name__ == '__main__':
    pass


