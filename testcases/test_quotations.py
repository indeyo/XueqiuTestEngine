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

    def test_get_hk_selected_stocks(self):
        hk_selected_stocks = self.quotations.get_hk_selected_stocks()
        assert "腾讯控股" in hk_selected_stocks
        assert "网易" not in hk_selected_stocks

    def test_get_us_selected_stocks(self):
        us_selected_stocks = self.quotations.get_us_selected_stocks()
        assert "网易" in us_selected_stocks

    def test_get_message(self):
        assert "今日话题" in self.quotations.goto_message().get_message_list()

    def test_market(self):
        pass
        # print(self.quotations.goto_market().get_hot_value())
        # assert self.quotations.goto_market().get_hot_value() > 90%