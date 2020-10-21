#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@file:redisUtils.py
@time:2020/09/27
"""
import redis

from common.logutil import LogUtil


# from loguru import logger

class RedisUtil(LogUtil):

    def __init__(self, host, port):

        try:
            self.r = redis.StrictRedis(host=host, port=port, decode_responses=True)
        except Exception as e:
            pass
            # self.logger.info("redis连接失败,错误信息为%s" %e)
            # print("redis连接失败,错误信息为%s" %e)

    def get_str(self, key):
        res = self.r.get(key)
        return res

    def set_str(self, key, value):
        self.r.set(key, value)

    def test(self):
        self.info("redis测试")
        # logger.info("redis测试")


if __name__ == '__main__':
    redis_host = "10.20.1.196"
    redis_port = 6379
    r = RedisUtil(redis_host, redis_port)
    r.test()
    # print(redis)
    # res= redis.get_str(key)
    # print(res)
    # key1 = "1"
    # key = r"register:email:verify:code:142145555@qq.com"
    # print(key)
    #
    # res= redis.get_str(key)
    # print(res)
    # print(type(res))
