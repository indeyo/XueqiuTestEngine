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
from pages.web_pages.stock import StockPage


class IndexPage(BasePage):
    _base_url = "https://xueqiu.com/"
    _search_locator = (By.CSS_SELECTOR, "[placeholder='搜索']")

    def search(self, key, stock_type):
        self.find(self._search_locator).send_keys(key)
        # 调试用
        # print(self._driver.window_handles)
        self.find(By.PARTIAL_LINK_TEXT, stock_type).click()
        # print(self._driver.window_handles)
        self.switch_window()
        return StockPage(self._driver)

    def goto_trade_funds(self):
        pass

    def goto_quotations(self):
        pass
