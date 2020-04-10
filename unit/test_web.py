# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : test_web.py
@Time    : 2020-04-09  15:26:14
@Author  : indeyo_lin
"""
import json

from pages.web import Web


class TestWeb:
    def setup(self):
        self.index = Web()
        # init不可用
        # self.index = Web()

    def test_save_cookies(self):
        self.index.start().save_cookies()
        # print(self.index)
        with open("D:\project\XueqiuTestEngine\config\cookies.json") as f:
            cookies = json.load(f)
        # print(cookies)
        assert cookies is not None

    def test_start_with_cookies(self):
        assert "发帖" in self.index.start_with_cookies().check_if_login()

    def teardown(self):
        self.index.quit()