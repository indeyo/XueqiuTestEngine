# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : search.py
@Time    : 2020-04-06  09:45:56
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    _input_locator = (By.ID, "search_input_text")
    _stocks_locator = (By.ID, "stockName")
    _close_locator = (By.ID, "action_close")

    def search(self, key, stock_type):
        self.find(self._input_locator).send_keys(key)
        self.find_by_text(stock_type).click()
        return self

    def add_stock(self):
        pass

    def check_if_selected(self):
        pass

    def get_all_stocks(self):
        all_stocks = self.find_elements_and_get_text(self._stocks_locator)
        self.find(self._close_locator).click()
        return all_stocks
