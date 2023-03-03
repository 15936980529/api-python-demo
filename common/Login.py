# -*- coding: utf-8 -*-
# @Time: 2023/3/2 23:14
# @Author: 闻道中人
# @Software: PyCharm
from utils.HttpClientUtil import HttpClientUtil
import requests.utils


def login(username, password, j_password):
    url = "/login"
    params = {"username": username, "password": password, "validcode": "", "j_password": j_password, "orgid": ""}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/110.0.0.0 Safari/537.36"}
    res = HttpClientUtil().post(url=url, headers=headers, params=params)
    cookies = res.cookies
    cookie = requests.utils.dict_from_cookiejar(cookies)
    print(cookie)
    return cookie
