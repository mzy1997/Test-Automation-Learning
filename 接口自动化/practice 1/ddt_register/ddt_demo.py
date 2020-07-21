# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Author:       MuZhengYan
# Name:         ddt_demo
# Description:  ddt的简单应用
# Author:       穆峥言
# Date:         2020/7/20
# File    :     ddt_demo.py
# Software:     PyCharm
# -------------------------------------------------------------------------------
import ddt
import unittest
import requests

data = [{"username": "keyou53217171912",
         "email": "keyou5497371291@qq.com",
         "password": "123456",
         "password_confirm": "123456",
         },
        {"username": "keyou53214341912",
         "email": "keyou549444291@qq.com",
         "password": "123456",
         "password_confirm": "123456",
         },
        {"username": "keyou53215251912",
         "email": "keyou54955291@qq.com",
         "password": "123456",
         "password_confirm": "123456",
         }
        ]


@ddt.ddt
class TestUseDDT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("执行用例前\n")

    @classmethod
    def tearDownClass(cls):
        print("执行用例后")

    @ddt.data(*data)
    def test_case1(self, data):
        url = "http://api.keyou.site:8000/user/register/"
        res = requests.post(url, data)
        print(res.json())


if __name__ == '__main__':
    unittest.main()
