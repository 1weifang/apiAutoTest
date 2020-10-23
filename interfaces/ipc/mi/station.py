#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@Description:基站模块相关接口
@file:station.py
@time:2020/09/28
"""

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common.baseutil import BaseUtil
from interfaces.common.send_post_requests import SendPostRequests
from config.ipc.mi.station import CHECK_IN_BIND_URL
from config.ipc.mi.station import LOCK_URL
from config.ipc.mi.station import ADD_URL
from config.ipc.mi.station import REMOVE_URL
from config.ipc.mi.station import SET_URL
from config.ipc.mi.station import REPORT_STATUS_URL
from config.ipc.mi.station import REPORT_ATTR_URL
from config.ipc.mi.station import REPORT_MONITOR_URL


class Station(SendPostRequests):


    def __init__(self):
        super().__init__()
        self.base = BaseUtil()


    def get_check_bind_status_url(self,access_token):
        '''
        定义校验基站绑定状态的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" +CHECK_IN_BIND_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_check_bind_status_data(self,stationSn):
        '''
        定义校验基站绑定状态的body
        :param stationSn:
        :return:
        '''
        data = {
            "stationSn":stationSn
        }
        return data

    # def get_station_login_url(self):
    #     '''
    #     定义基站登录URL
    #     :return:
    #     '''
    #     url = "https://iot-api-test.sunvalleycloud.com/oauth/login"
    #     return url
    #
    # def get_station_login_data(self,stationSn):
    #     '''
    #     定义基站登录body
    #     :param stationSn:
    #     :return:
    #     '''
    #     data = {
    #             "client_id": "9c33e08830c243c597246c71e3c2f458",
    #             "client_secret": "237e61fdc48a46908736c499685e9f34",
    #             "scope": "all",
    #             "grant_type": "password",
    #             "sn": stationSn,
    #             "auth_type": "sn_password"
    #             }
    #     return data



    def get_lock_url(self,access_token):
        '''
        定义基站进入配对模式【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://iot-api-test.sunvalleycloud.com" +  LOCK_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_lock_data(self):
        '''
        定义基站进入配对模式【基站】的data
        :return:
        '''
        data = {

        }
        return data

    def get_add_url(self,access_token):
        '''
        定义添加基站的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + ADD_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
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

    def get_remove_url(self,access_token):
        '''
        定义移除基站的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REMOVE_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
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

    def get_set_url(self,access_token):
        '''
        定义设置基站的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + SET_URL +  "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
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


    def get_report_status_url(self,access_token):
        '''
        定义上报状态【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REPORT_STATUS_URL +  "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_report_status_data(self):
        '''
         定义上报状态【基站】的body
        :param stationSn:
        :return:
        '''
        data = {
                "stationStatusObject": {
                    "xxxxxx": "xxxxxx",
                    "yyyyyy": "yyyyyy"
                },
                "cameraStatusObjectList": [
                    {
                        "cameraSn": "P020101000101020000000001",
                        "powerLever": 66
                    }
                ]
                }

        return data




    def get_report_attr_url(self,access_token):
        '''
        定义上报属性【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REPORT_ATTR_URL +  "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_report_attr_data(self):
        '''
         定义上报属性【基站】的body
        :param stationSn:
        :return:
        '''
        data = {
                "stationAttrObject": {
                    "aaaaaa": "mock1",
                    "bbbbbb": "mock"
                },
                "cameraAttrObject": {
                    "cameraSn": "P020101000101020000000001",
                    "xxxxxx": "mock1",
                    "yyyyyy": "mock"
                }
                }
        return data


    def get_report_monitor_url(self,access_token):
        '''
        定义上报布防【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REPORT_MONITOR_URL +  "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_report_monitor_data(self):
        '''
         定义上报布防【基站】的body
        :param stationSn:
        :return:
        '''
        data = {
                "cameraMonitorObject": [{
                    "cameraSn": "P020101000101020000000001",
                    "arminglist": [{
                        "days": "0123456",
                        "endtime": "235959",
                        "starttime": "000000"
                    }, {
                        "days": "0246",
                        "endtime": "020000",
                        "starttime": "013000"
                    }],
                    "channel": 1,
                    "type": 2
                }]
                }
        return data

if __name__ == '__main__':
    pass
