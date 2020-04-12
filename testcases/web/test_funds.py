# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : test_funds.py
@Time    : 2020-04-11  17:19:19
@Author  : indeyo_lin
"""
from pages.web import Web


class TestFunds:
    def setup(self):
        self.funds = Web().start_with_cookies().index_page().goto_trade_funds()

    def test_login_fail(self):
        assert "验证码已过期" in self.funds.goto_login().login_by_code_fail("13800000000", "123456")

    def teardown(self):
        self.funds.quit()