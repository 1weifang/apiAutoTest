#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:描述
@file:test.py
@time:2020/10/20
"""
from common.redisutil import RedisUtil
from common.mysqlutil import MysqlUtil




redis_host = "10.20.1.196"
redis_port = 6379
r = RedisUtil(redis_host, redis_port)

r.test()

