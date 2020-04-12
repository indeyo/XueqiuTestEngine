# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : hq_center.py
@Time    : 2020-04-12  08:37:45
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HQCenterPage(BasePage):
    _first_stock_quote = (By.CSS_SELECTOR, ".detail-container>div>div>a")

    def get_first_stock_quote(self):
        return self.find_element_and_get_text(self._first_stock_quote)