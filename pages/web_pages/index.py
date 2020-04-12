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
from pages.web_pages.funds import FundsPage
from pages.web_pages.stock import StockPage


class IndexPage(BasePage):
    _base_url = "https://xueqiu.com/"
    _search_locator = (By.CSS_SELECTOR, "[placeholder='搜索']")
    _funds_locator = (By.CSS_SELECTOR, ".nav__menu>div:nth-child(5) a:nth-child(3)")
    _trade_locator = (By.CSS_SELECTOR, ".nav__menu>div:nth-child(5)")

    def search(self, key, stock_type):
        self.find(self._search_locator).send_keys(key)
        # 调试用
        # print(self._driver.window_handles)
        self.find(By.PARTIAL_LINK_TEXT, stock_type).click()
        # print(self._driver.window_handles)
        self.switch_to_window()
        return StockPage(self._driver)

    def goto_trade_funds(self):
        # 确认 蛋卷基金 元素在页面内
        # print(self._driver.page_source)
        # 尽管 蛋卷基金 在页面内，但是必须点开 交易 下拉框，才能定位到，这是为啥呢？？selenium长眼睛？
        self.find(self._trade_locator).click()
        self.find(self._funds_locator).click()
        # 进入蛋卷基金新页面，需要切换窗口
        self.switch_to_window()
        return FundsPage(self._driver)

    def goto_quotations(self):
        pass
