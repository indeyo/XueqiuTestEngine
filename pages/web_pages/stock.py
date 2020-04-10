# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : stock.py
@Time    : 2020-04-10  11:17:55
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class StockPage(BasePage):
    _add_locator = (By.CSS_SELECTOR, ".follow")
    _no_share_locator = (By.LINK_TEXT, "取消")
    _selected_locator = (By.CSS_SELECTOR, ".stock-operate>a")
    _stock_price_locator = (By.CSS_SELECTOR, ".stock-current strong")

    def get_price(self):
        price = self.find_element_and_get_text(self._stock_price_locator)
        # 去掉单位，返回股价浮点型
        return float(price.partition("$")[-1])

    def add_stock(self):
        # 调试用
        # print(self._driver.window_handles)
        # print(self._driver.page_source)
        self.find(self._add_locator).click()
        self.find(self._no_share_locator).click()
        return self

    def unselect_stock(self):
        pass

    def check_if_selected(self):
        selected_btn = self.find(self._selected_locator)
        if "followed" in selected_btn.get_attribute("class"):
            # 如果已选，则取消
            selected_btn.click()
        return self