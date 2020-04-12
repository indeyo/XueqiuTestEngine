# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : test_hq_center.py
@Time    : 2020-04-12  09:05:04
@Author  : indeyo_lin
"""
from pages.web import Web


class TestHQCenter:
    def setup(self):
        self.page = Web().start_with_cookies().index_page().goto_hq_center()

    def test_quotations(self):
        assert "上证指数" in self.page.get_first_stock_quote()