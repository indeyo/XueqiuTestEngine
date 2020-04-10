# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : index.py
@Time    : 2020-04-09  11:03:58
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class IndexPage(BasePage):
    _base_url = "https://xueqiu.com/"
    _search_locator = (By.CSS_SELECTOR, "[placeholder='搜索']")

    def search(self):
        self.find()

    def goto_trade_funds(self):
        pass

    def goto_quotations(self):
        pass