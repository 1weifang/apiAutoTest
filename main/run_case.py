#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:42
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : run_case.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest



# 用例路径
case_path = os.path.join(os.getcwd())
# print(case_path)
# 报告存放路径
report_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'report')

log_path = base.getProjectPath()+os.sep+"report"+os.sep

def getenv():
    env = sys.argv[1]
    return env



def find_new_file(report_path):
    '''查找目录下最新的文件'''
    file_lists = os.listdir(report_path)
    file_lists.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn)
                    if not os.path.isdir(report_path + "\\" + fn) else 0)
    # print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(report_path, file_lists[-1])
    # print('完整路径：', file)
    return file


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_case_*.py", top_level_dir=None)
    return discover


def  run(testSuit):
    result = BeautifulReport(testSuit)
    result.report(filename=filename, description='tutuAndroidAutoTest接口自动化测试报告', log_path="../report")
    return result

if __name__ == "__main__":
    testSuit = all_case()
    result = run(testSuit)
    errorNumber = result.error_count
    start_time = result.begin_time
    s = result.start_time
    totalTime = result.stopTestRun().get("totalTime")











