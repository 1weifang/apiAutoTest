#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:消息中心模块测试用例
@file:msg_center_test.py
@time:2020/10/22
"""
import sys,os

import pytest


from testcases.conftest import mi_token

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from interfaces.ipc.mi.msg_center import MsgCenter

class Test_MsgCenter:


    def setup(self):
        self.mc = MsgCenter()

    def test_MsgCenter_condition(self):
        condition_url = self.mc.get_condition_url(mi_token)
        condition_data = self.mc.get_condition_data()
        self.mc.send_post_requests(condition_url,condition_data)


    def test_MsgCenter_page(self):
        page_url = self.mc.get_page_url(mi_token)
        page_data = self.mc.get_page_data()
        self.mc.send_post_requests(page_url,page_data)


if __name__ == '__main__':
    pytest.main(['-s', "msg_center_test.py"])