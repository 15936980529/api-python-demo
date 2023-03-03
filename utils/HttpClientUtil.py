# -*- coding: utf-8 -*-
# @Time: 2023/3/2 23:30
# @Author: 闻道中人
# @Software: PyCharm
from utils.ReadYamlUtil import read_yaml
import requests
import os


class HttpClientUtil:
    # 默认请求头,防止越权
    default_header = {"Referer": "http://cooffoo.fat.qa.pab.com.cn/morone/qwer/index.html"}

    def __int__(self):
        """
        读取env.yaml环境配置文件,获取默认请求地址
        """
        project_name = r"api-python_demo"
        envYaml_path = r"\config\env.yaml"
        file_path = os.path.abspath(os.path.dirname(__file__))
        config_env_path = file_path[:file_path.index(project_name) + len(project_name)] + envYaml_path
        result = read_yaml(config_env_path)
        self.baseurl = result["FAT001"]["host"]

    def get(self, url, headers=None, params=None, cookies=None):
        if headers is None:
            headers = self.default_header
        res = requests.get(self.baseurl + url, headers=headers, params=params, cookies=cookies)
        print("请求地址:{}".format(res.url))
        print("请求头信息:{}".format(headers))
        print("请求参数params:{}".format(params))
        print("响应信息:{}".format(res.json()))
        return res

    def post(self, url, headers=None, params=None, json=None, data=None, cookies=None, files=None):
        if headers is None:
            headers = self.default_header
        # 如果有上传excel文件,requests库会自动添加这个请求头{"Content-Type":"multipart/form-data"}。加了反而会报错，从而导致请求不成功。
        # 如果上传的文件携带了参数则需要传入data={"参数名1":"值1"},否则只传入files即可
        res = requests.post(self.baseurl+url, headers=headers, params=params, json=json, data=data, cookies=cookies, files=files)
        print("请求地址:{}".format(res.url))
        print("请求头信息:{}".format(headers))
        print("请求参数param:{}".format(params))
        print("请求参数json:{}".format(json))
        print("请求参数data:{}".format(data))
        print("响应信息:{}".format(res.json()))
        return res
