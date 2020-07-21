# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Author:       MuZhengYan
# Name:         unittest_register
# Description:  unitTest完成用户注册、重复用户名、邮箱格式错误三个用例的编写
# Author:       穆峥言
# Date:         2020/7/20
# File    :     unittest_register.py
# Software:     PyCharm
# -------------------------------------------------------------------------------
import unittest
import requests
import random


class TestReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg_url = "http://api.keyou.site:8000/user/register/"
        cls.reg_data = {"username": "keyou5321221912",
                         "email": "keyou549111291@qq.com",
                         "password": "123456",
                         "password_confirm": "123456",
                        }

    @classmethod
    def tearDownClass(cls):
        print("用例执行完毕")

    # Case1: 用户输入正确的用户名、邮箱、密码完成注册
    def test_case1(self):
        res = requests.post(self.reg_url, self.reg_data)
        self.assertEqual(res.status_code, 201, "Case1: 用户输入正确的用户名、邮箱、密码完成注册失败")

    # Case2: 用户使用重复的用户名注册
    def test_case2(self):
        # 注册数据字典浅复制
        data_dic = self.reg_data.copy()
        # 修改data里email字段的值，保证只有用户名相同
        data_dic["email"] = str(random.randint(0, 100)) + data_dic["email"]
        res = requests.post(self.reg_url, data_dic)
        self.assertEqual(res.status_code, 201, "Case2: 已存在一位使用该名字的用户")

    # Case3: 邮箱格式有误
    def test_case3(self):
        # 注册数据字典浅复制
        data_dic = self.reg_data.copy()
        # 修改data里email字段的值，保证只有用户名相同
        data_dic["email"] = "@" + data_dic["email"]
        res = requests.post(self.reg_url, data_dic)
        self.assertEqual(res.status_code, 201, "Case3: 邮箱格式有误")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_cases = [TestReg("test_case1"), TestReg("test_case2"), TestReg("test_case3")]
    suite.addTests(test_cases)
    # 执行测试
    # verbosity=2,测试结果的输出的详细程度，有0-6级
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
