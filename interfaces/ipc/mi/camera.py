#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:durant.zeng
@file:camera.py
@time:2020/09/29
"""

from interfaces.common.send_post_requests import SendPostRequests
import sys,os
from common.baseutil import BaseUtil
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config.ipc.mi.camera import CHECK_BIND_STATUS
from config.ipc.mi.camera import ADD_BIND_URL
from config.ipc.mi.camera import ADD_URL
from config.ipc.mi.camera import REMOVE_URL
from config.ipc.mi.camera import SET_URL
from config.ipc.mi.camera import LIST_FOR_STATION_URL
from config.ipc.mi.camera import LIST_FOR_INDEX_URL
from config.ipc.mi.camera import LIST_FOR_MGT_URL
from config.ipc.mi.camera import LIST_FOR_MY_DEVICES_URL
from config.ipc.mi.camera import LIST_FOR_SHARE_URL
from config.ipc.mi.camera import LIST_SN_STATUS




class camera(SendPostRequests):

    def __init__(self):
        super().__init__()
        self.base = BaseUtil()

    def get_check_bind_status_url(self,access_token):
        '''
        定义校验摄像头绑定状态的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + CHECK_BIND_STATUS + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_check_data(self,cameraSn,stationSn):
        '''
        定义校验摄像头绑定状态的body
        :param stationSn:
        :return:
        '''
        data = {
            "cameraSn":cameraSn,
            "stationSn":stationSn,
            "channel":0
        }
        return data

    def get_add_blind_url(self,access_token):
        '''
        定义盲配添加摄像头【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://iot-api-test.sunvalleycloud.com" +  ADD_BIND_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_add_blind_data(self,cameraSn):
        '''
        定义盲配添加摄像头【基站】的data
        :return:
        '''
        data = {
            "cameraSn":cameraSn,
            "cameraName":"",
            "channel":0
        }
        return data

    def get_add_url(self,access_token):
        '''
        定义正常添加摄像头【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + ADD_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_add_data(self,cameraSn):
        '''
         定义正常添加摄像头【基站】的body
        :param cameraSn:
        :return:
        '''
        data = {
            "cameraSn":cameraSn,
            "cameraName":"",
            "channel":0
        }
        return data


    def get_remove_url(self,access_token):
        '''
        定义移除摄像头的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + REMOVE_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_remove_data(self,cameraSn):
        '''
         定义移除摄像头的body
        :param cameraSn:
        :return:
        '''
        data = {
            "cameraSn":cameraSn
        }
        return data


    def get_set_url(self,access_token):
        '''
        定义设置摄像头的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + SET_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_set_data(self,cameraSn,shareFlag,cameraName,voiceSwitch,mailSwitch,pushSwitch):
        '''
         定义设置摄像头的body
        :param cameraSn:
        :return:
        '''
        data = {
            "cameraSn":cameraSn,
            "shareFlag":shareFlag,
            "cameraName":cameraName,
            "voiceSwitch":voiceSwitch,
            "mailSwitch":mailSwitch,
            "pushSwitch":pushSwitch
        }
        return data


    def get_list_for_station_url(self,access_token):
        '''
        定义查询摄像头列表【基站】的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LIST_FOR_STATION_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_list_for_station_data(self):
        '''
         定义查询摄像头列表【基站】的body
        :return:
        '''
        data = {
        }
        return data


    def get_list_for_index_url(self,access_token):
        '''
        定义查询摄像头列表-首页的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LIST_FOR_INDEX_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_list_for_index_data(self):
        '''
         定义查询摄像头列表-首页的body
        :return:
        '''
        data = {
        }
        return data



    def get_list_for_mgt_url(self,access_token):
        '''
        定义查询摄像头列表-管理的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LIST_FOR_MGT_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_list_for_mgt_data(self):
        '''
         定义查询摄像头列表-管理的body
        :return:
        '''
        data = {
        }
        return data


    def get_list_for_my_devices_url(self,access_token):
        '''
        定义查询摄像头列表-我的设备的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LIST_FOR_MGT_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_list_for_my_devices_data(self):
        '''
         定义查询摄像头列表-我的设备的body
        :return:
        '''
        data = {
        }
        return data


    def get_list_for_share_url(self,access_token):
        '''
        定义查询摄像头列表-分享的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LIST_FOR_SHARE_URL + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_list_for_share_data(self,receiverId=None):
        '''
         定义查询摄像头列表-分享的body
        :return:
        '''
        data = {
            "receiverId":receiverId
        }
        return data


    def get_list_sn_status_url(self,access_token):
        '''
        定义查询设备状态的URL
        :param access_token:
        :return:
        '''
        url = "https://mi-api-test.sunvalleycloud.com" + LIST_SN_STATUS + "?&access_token=%s&timeStamp=%s&lang=en" %(access_token,self.base.getTimeStamp())
        return url

    def get_list_sn_status_data(self,sn):
        '''
         定义查询设备状态的body
        :return:
        '''
        data = {
            "sn":sn
        }
        return data

if __name__ == '__main__':
    pass