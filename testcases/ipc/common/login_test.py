#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:登录模块的测试用例
@file:login_test.py
@time:2020/10/21
"""
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import pytest
import allure
from interfaces.ipc.common.login import Login


@allure.feature("登录功能")#feature定义功能
class Test_Login:

    def setup(self):
        self.login = Login()


    @allure.story("登录功能测试")#story定义用户场景
    @pytest.mark.parametrize("email",["115930@hyhpzengweifang.com.cn","asafasfasf",""])
    @pytest.mark.parametrize("password", ["5481349Aa",""])
    def test_login(self,email,password):
        login_url =  self.login.get_login_url()
        login_data =  self.login.get_login_data(email,password)
        self.login.send_post_requests(login_url,login_data)

    def teardown(self):
        pass

if __name__ == '__main__':
    pytest.main(['-s',"login_test.py"])