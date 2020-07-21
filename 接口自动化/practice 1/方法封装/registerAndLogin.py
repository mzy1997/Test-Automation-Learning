# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Author:       MuZhengYan
# Name:         registerAndLogin
# Description:  注册与登录接口自动化
# Author:       穆峥言
# Date:         2020/7/18
# File    :     registerAndLogin.py
# Software:     PyCharm
# -------------------------------------------------------------------------------
import requests
import sys
import json


# 注册
class Register:

    def register(self, url, data, method, token=None, cookie=None):
        """
        :param url:              请求地址
        :param data:             请求参数
        :param method:           请求方法类型
        :param token:            令牌
        :param cookie:           cookies
        :return:res              登录响应体
        """
        try:
            # GET
            if method.upper() == "GET":
                res = requests.get(url, data)
            # POST
            elif method.upper() == "POST":
                res = requests.post(url, data)
            # PUT
            elif method.upper() == "PUT":
                res = requests.put(url, data)
            # DELETE
            elif method.upper() == "DELETE":
                res = requests.delete(url, data)
            else:
                res = "fail"
                return res
        except Exception as e:
            print("注册发生错误,%s" % e.args)
        else:
            return res


# 登录
class Login:

    def login(self, url, data, method, token=None, cookie=None):
        """
        :param url:              请求地址
        :param data:             请求参数
        :param method:           请求方法类型
        :param token:            令牌
        :param cookie:           cookies
        :return:res              登录响应体
        """

        headers = {"token": token,
                   "cookies": cookie}

        try:
            # GET
            if method.upper() == "GET":
                res = requests.get(url, data, headers=headers)
            # POST
            elif method.upper() == "POST":
                res = requests.post(url, data, headers=headers)
            # PUT
            elif method.upper() == "PUT":
                res = requests.put(url, data, headers=headers)
            # DELETE
            elif method.upper() == "DELETE":
                res = requests.delete(url, data, headers=headers)
            # 除4种常用请求类型以外的、以及不合法的参数
            else:
                res = "fail"
                return res
        except Exception as e:
            print("登录发生错误，%s" % e.args)
        else:
            return res


if __name__ == '__main__':
    # 注册所需参数
    reg_url = "http://api.keyou.site:8000/user/register/"
    reg_data = {"username": "keyou52191",
                "email": "keyou5299@qq.com",
                "password": "123456",
                "password_confirm": "123456",
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1NjgsInVzZXJuYW1lIjoia2V \
                          5b3U1MjAiLCJleHAiOjE1ODMzNzk2NjIsImVtYW lsIjoia2V5b3U1MjBAcXEuY29tIn0.4qOcs1 \
                          QSe3mK1KlB7DQiKnBd1vJelakl_Xd5fxroc6U"}
    reg_method = "post"

    reg_res = Register().register(reg_url, reg_data, reg_method)
    # 注册返回结果判断
    if type(reg_res) != str:
        print(json.dumps(reg_res.json(), sort_keys=True, indent=4))
    else:
        print(reg_res)
        sys.exit(0)

    token = ""
    # 注册成功，状态码为201，则赋值token
    if reg_res.status_code == 201:
        reg_res_dict = dict(reg_res.json())
        token = reg_res_dict["token"]
    else:
        print("注册失败,状态码:%d" % reg_res.status_code)

    # 登录所需参数
    login_url = "http://api.keyou.site:8000/user/login/"
    login_data = {"username": reg_data["username"],
                  "password": reg_data["password"]}
    login_method = "post"
    login_res = Login().login(login_url, login_data, login_method, token)
    # 登录返回结果判断
    if type(login_res) != str:
        print("登录响应:")
        print(json.dumps(login_res.json(), sort_keys=True, indent=4))
    else:
        print(login_res)



