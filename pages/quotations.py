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
from pages.message import MessagePage
from pages.search import SearchPage


class QuotationsPage(BasePage):
    _search_locator = (By.ID, "action_search")
    _selected_stocks_locator = (By.ID, "portfolio_stockName")
    _message_locator = (By.ID, "action_message")
    _market_locator = (By.XPATH, "//*[@text='市场' and contains(@resource-id, 'title_text')]")
    _hot_value_locator = (By.ID, "hot_value")

    def goto_market(self):
        self.find(self._market_locator).click()
        return self

    def goto_search(self):
        self.find(self._search_locator).click()
        return SearchPage(self._driver)

    def goto_message(self):
        self.find(self._message_locator).click()
        return MessagePage(self._driver)

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
        return self.find_elements_and_get_text(self._selected_stocks_locator)

    def get_hk_selected_stocks(self):
        self.find_by_text("港股").click()
        return self.find_elements_and_get_text(self._selected_stocks_locator)

    def get_us_selected_stocks(self):
        self.find_by_text("美股").click()
        return self.find_elements_and_get_text(self._selected_stocks_locator)

    def get_single_line_quote_price(self):
        pass

    def get_single_line_quote_pct(self):
        pass

    def goto_main(self):
        self.find_by_text("雪球").click()
        return MainPage(self._driver)

    def get_hot_value(self):
        return self.find_element_and_get_text(self._hot_value_locator)
