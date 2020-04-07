# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : quotations.py
@Time    : 2020-04-06  09:45:39
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main import MainPage
from pages.search import SearchPage


class QuotationsPage(BasePage):
    _search_locator = (By.ID, "action_search")

    def goto_market(self):
        pass

    def goto_search(self):
        self.find(self._search_locator).click()
        return SearchPage(self._driver)

    def goto_message(self):
        pass

    def goto_settings(self):
        pass

    def goto_stock_fund(self):
        pass

    def goto_uncommon_event(self):
        pass

    def goto_stock_transaction(self):
        pass

    def goto_stock_news(self):
        pass

    def get_all_selected_stocks(self):
        pass

    def get_hk_selected_stocks(self):
        pass

    def get_us_selected_stocks(self):
        pass

    def get_single_line_quote_price(self):
        pass

    def get_single_line_quote_pct(self):
        pass

    def goto_main(self):
        self.find_by_text("雪球").click()
        return MainPage(self._driver)
