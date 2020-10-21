import hashlib
import time
import datetime
import random
import string
import sys, os

class BaseUtil:
    def __init__(self):
        pass

    @classmethod
    def MD5(self,str):
        '''
        :param str:
        :return: MD5 encryption
        '''
        m = hashlib.md5()
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    @classmethod
    def getTimeStamp(self):
        '''
        :return: str
        '''
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tempList = now.split(" ")
        return ("".join(tempList[0].split("-")) + "".join(tempList[1].split(":")))


    def timestamp_to_str(self,timeStamp=None, format='%Y-%m-%d %H:%M:%S'):
        if timeStamp:
            time_tuple = time.localtime(timeStamp)  # 把时间戳转换成时间元祖
            result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
            return result
        else:
            return time.strptime(format)


    def str_to_timestamp(self,str_time=None, format='%Y-%m-%d %H:%M:%S'):
        if str_time:
            time_tuple = time.strptime(str_time, format)  # 把格式化好的时间转换成元祖
            result = time.mktime(time_tuple)  # 把时间元祖转换成时间戳
            return int(result)
        return int(time.time())



    def get_random_string(self,number):
        '''只能产生最多50'''
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, number))
        return  ran_str


    def get_millisecond(self):
        millis = int(round(time.time() * 1000))
        return millis

    def get_miniRectWidth(self):
        number = random.randint(100,130)
        return number


    def str2int(self,str):
        return int(str)


    def getToDay(self):
        return datetime.date.today()


    def chooseTwoAgentId(self,dict):
        if dict["supplierCompanyName"] == "深圳市丹芽科技":
            return dict["twoAgentId"]
        else:
            return None

    def choosePlan(self,dict):
        if dict["title"] == "美甲机租赁":
            return dict["id"]
        else:
            return None



    def getProjectPath(self):
        #projectName = "AnjouAutotest"
        projectName = "webrtcTest"
        projectPath = os.path.dirname(os.path.abspath('.'))
        aList = projectPath.split(projectName)
        bList = aList[0].split(os.sep)
        reallyProject = os.sep.join(bList[0:-1])+os.sep+projectName
        return reallyProject


    def get_deviceID(self,dict):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get('sn')
                if res != None:
                    result.append(lst.get('id'))
        except:
            raise Exception('error')
        finally:
            return result

    def get_nailSuitStatus_for_1(self,dict):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get('nailSuitStatus')
                if res == 1:
                    result.append(lst.get('albumsId'))
        except:
            raise Exception('error')
        finally:
            return result



if __name__ == "__main__":
    pass



