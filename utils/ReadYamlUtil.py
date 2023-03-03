# -*- coding: utf-8 -*-
# @Time: 2023/3/2 23:15
# @Author: 闻道中人
# @Software: PyCharm

# 读取yaml
import yaml


def read_yaml(filepath):
    with open(filepath, mode="r", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value
