#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@file:register.py
@time:2020/09/28
"""
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common.baseutil import BaseUtil
from interfaces.common.send_post_requests import SendPostRequests
from config.ipc.common.common_urls import REGISTER_AUTH_URL
from config.ipc.common.common_urls import REGISTER_EMAIL_VERIFY
from config.ipc.common.common_urls import REGISTER_SEND_EMAIL_VERIFY_CODE
from config.ipc.common.common_urls import REGISTER_EMAIL_PASSWORD

class Register(SendPostRequests):

    def __init__(self):
        super().__init__()
        self.base=BaseUtil()


    def get_login_auth_url(self,mi_base_url):
        '''
        定义鉴权登录的URL
        :param timestamp:
        :return:
        '''
        url = mi_base_url + REGISTER_AUTH_URL + "?&timeStamp=%s&lang=en" %(self.base.getTimeStamp())
        return url


    def get_login_auth_data(self):
        '''
        定义鉴权登录的body
        :return:
        '''
        data = {
            "client_id": "0778a347853545c08d496566e0d0180c",
            "client_secret": "a0b5ca0e003a398fc4793514b0b3f754",
            "grant_type": "client_credentials",
            "scope": "all"
                }
        return data

    def get_email_verify_url(self,access_token):
        '''
        定义邮箱校验接口的URL
        :param timestamp:
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REGISTER_EMAIL_VERIFY + "?&timeStamp=%s&lang=en&access_token=%s" % (self.base.getTimeStamp(),access_token)
        return url

    def get_email_verify_data(self,email):
        '''
        定义邮箱校验接口的body
        :param email:
        :return:
        '''
        data = {
            "email":email
        }
        return data

    def get_send_code_url(self,access_token):
        '''
        定义邮箱发送验证码的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REGISTER_SEND_EMAIL_VERIFY_CODE + "?&timeStamp=%s&lang=en&access_token=%s" % (self.base.getTimeStamp(),access_token)
        return url

    def get_send_code_data(self,email):
        '''
        定义发送验证码的body
        :param email:
        :return:
        '''
        data = {
            "email":email
        }
        return data

    def get_email_passwd_register_url(self,access_token):
        '''
        定义邮箱密码注册的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REGISTER_EMAIL_PASSWORD + "?&timeStamp=%s&lang=en&access_token=%s" % (self.base.getTimeStamp(),access_token)
        return url


    def get_email_passwd_register_data(self,email,verifyCode):
        '''
        定义邮箱密码注册的body
        :param email:
        :param verifyCode:
        :return:
        '''

        data = {
            "email":email,
            "firstName": "durant",
            "lastName": "zeng",
            "password": "2868fc65d8ee171b213488ab47a5b36e",
            "productLineId": "4f975dc1a43d4117a6f3eb83b2cbc778",
            "verifyCode": verifyCode
                }
        return data


if __name__ == '__main__':
    pass
