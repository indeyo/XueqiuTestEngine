# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : test_stock.py
@Time    : 2020-04-10  14:35:08
@Author  : indeyo_lin
"""
from pages.web import Web


class TestStock:
    def setup(self):
        self.page = Web().start_with_cookies()

    def test_add_stock(self):
        assert self.page.index_page().search("alibaba", "BABA").check_if_selected().add_stock().get_price() < 200

    def teardown(self):
        self.page.quit()