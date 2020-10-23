#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:定义统一的mi用户登录以及iot设备登录
@file:conftest.py
@time:2020/10/22
"""
import pytest
from interfaces.ipc.common.login import Login
email = "115930@hyhpzengweifang.com.cn"
password = "5481349Aa"
#定义整个测试用例执行的时间,单位为s
testcases_execult_time = 300
login = Login()
# @pytest.fixture(scope="session")
def mi_token():
    login_url = login.get_mi_login_url()
    login_data =login.get_mi_login_Android_email_password_data(email, password)
    login_res = login.send_post_requests(login_url, login_data)
    #登录的access_token值
    access_token = login_res["data"]["access_token"]
    #登录的refresh_token值
    refresh_token = login_res["data"]["refresh_token"]
    #如果登录的access_token值不足以支持整个测试用例跑完，则生成新的access_token
    if login_res["data"]["expires_in"] < testcases_execult_time:
        refresh_token_url = login.get_mi_refresh_token_url()
        refresh_token_data = login.get_mi_refresh_token_data(refresh_token)
        refresh_token_res = login.send_post_requests(refresh_token_url,refresh_token_data)
        access_token = refresh_token_res["data"]["access_token"]
        return access_token
    else:
        return access_token
mi_token = mi_token()



