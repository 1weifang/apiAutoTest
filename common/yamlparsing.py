
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import yaml


class YamlParser:

    def __init__(self, fileName):
        '''
        :param fileName:
        '''
        self.logger = Logger(logger="yamlParser").getlog()
        self.fileName = fileName

    def load(self):
        '''返回一个字典'''
        result = yaml.load(open(self.fileName),Loader=yaml.FullLoader)
        return result
        # return json.loads(result, indent=2)

    def get_test_all_devicesList(self):
        '''获取所有的测试设备名称，返回一个list'''
        devices = self.load()
        devicesList = list(devices.keys())
        self.logger.info("所有的测试设备为:%s" %str(devicesList))
        return devicesList


if __name__ == "__main__":
    pass
    # config = yamlParser(r'D:\learn\webrtcTest\config\devices.yaml')






