#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@file:station.py
@time:2020/09/28
"""

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common.baseutil import BaseUtil
from interfaces.common.send_post_requests import SendPostRequests


class station(SendPostRequests):


    def __init__(self):
        super().__init__()


    def get_check_url(self,access_token,timeStamp):
        '''
        定义校验基站绑定状态的URL
        :param access_token:
        :param timeStamp:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com/ipc/device/station/check-bind-status?&access_token=%s&timeStamp=%s&lang=en" %(access_token,timeStamp)
        return url

    def get_check_data(self,stationSn):
        '''
        定义校验基站绑定状态的body
        :param stationSn:
        :return:
        '''
        data = {
            "stationSn":stationSn
        }
        return data

    def get_station_login_url(self):
        '''
        定义基站登录URL
        :return:
        '''
        url = "https://iot-api-test.sunvalleycloud.com/oauth/login"
        return url

    def get_station_login_data(self,stationSn):
        '''
        定义基站登录body
        :param stationSn:
        :return:
        '''
        data = {
                "client_id": "9c33e08830c243c597246c71e3c2f458",
                "client_secret": "237e61fdc48a46908736c499685e9f34",
                "scope": "all",
                "grant_type": "password",
                "sn": stationSn,
                "auth_type": "sn_password"
                }
        return data

    def get_lock_url(self,access_token,timeStamp):
        '''
        定义基站进入配对模式【基站】的URL
        :param access_token:
        :param timeStamp:
        :return:
        '''
        url = "https://iot-api-test.sunvalleycloud.com/ipc/device/station/lock?&access_token=%s&timeStamp=%s&lang=en" %(access_token,timeStamp)
        return url

    def get_lock_data(self):
        '''
        定义基站进入配对模式【基站】的data
        :return:
        '''
        data = {}
        return data

    def get_add_url(self,access_token,timeStamp):
        '''
        定义添加基站的URL
        :param access_token:
        :param timeStamp:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com/ipc/device/station/add?&access_token=%s&timeStamp=%s&lang=en" %(access_token,timeStamp)
        return url

    def get_add_data(self,stationSn):
        '''
         定义添加基站的body
        :param stationSn:
        :return:
        '''
        data = {
            "stationName":"",
            "stationSn":stationSn
        }
        return data

    def get_remove_url(self,access_token,timeStamp):
        '''
        定义移除基站的URL
        :param access_token:
        :param timeStamp:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com/ipc/device/station/remove?&access_token=%s&timeStamp=%s&lang=en" %(access_token,timeStamp)
        return url

    def get_remove_data(self,stationSn):
        '''
         定义移除基站的body
        :param stationSn:
        :return:
        '''
        data = {
            "stationSn":stationSn
        }
        return data

    def get_set_url(self,access_token,timeStamp):
        '''
        定义设置基站的URL
        :param access_token:
        :param timeStamp:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com/ipc/device/station/set?&access_token=%s&timeStamp=%s&lang=en" %(access_token,timeStamp)
        return url

    def get_set_data(self,stationSn,stationName):
        '''
         定义设置基站的body
        :param stationSn:
        :return:
        '''
        data = {
            "stationSn":stationSn,
            "stationName":stationName
        }
        return data


if __name__ == '__main__':
    st = station()
    base = baseUtils()
    stationsSNPath = r"D:\learn\IOT\CloudStorage\config\tidb-test-基站-5000.txt"
    stationsSNList = base.IPC_get_devices(stationsSNPath)
    station_login_url = st.get_station_login_url()
    for station in stationsSNList:
        station_login_data = st.get_station_login_data(station)
        station_login_res = st.send_post_requests(station_login_url,station_login_data)
        print(station_login_res["data"]["access_token"])
