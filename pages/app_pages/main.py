# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : main.py
@Time    : 2020-04-06  10:02:24
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.app_pages.search import SearchPage


class MainPage(BasePage):
    _search_locator = (By.ID, "tv_search")

    # def main(self):
    #     page_source=self._driver.page_source
    #     def wait_load(driver):
    #         if

    def goto_search(self):
        self.find(self._search_locator).click()
        return SearchPage(self._driver)

    def goto_quotations(self):
        # 解决循环调用问题
        from pages.app_pages.quotations import QuotationsPage
        self.find_by_text("行情").click()
        return QuotationsPage(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass
