#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:描述
@file:conftest.py
@time:2020/10/22
"""

import pytest

iaas={
    'mi_base_url':'https://mi-api-test.sunvalleycloud.com',
    'iot_base_url':'https://iot-api-test.sunvalleycloud.com'
}

@pytest.fixture(scope="module")
def com_variable():
    return iaas
