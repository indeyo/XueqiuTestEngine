# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : test_quotations.py
@Time    : 2020-04-06  11:21:37
@Author  : indeyo_lin
"""
from pages.app import App


class TestQuotations:
    def setup(self):
        self.quotations = App().start_app().goto_quotations()

    def test_search(self):
        assert "阿里巴巴" in self.quotations.goto_search().search("alibaba", "BABA").get_all_stocks()
