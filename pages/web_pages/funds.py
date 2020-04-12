# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : funds.py
@Time    : 2020-04-11  16:16:35
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FundsPage(BasePage):
    _base_url = "https://danjuanfunds.com/"
    _login_locator = (By.CSS_SELECTOR, ".login")
    _telephone_num_locator = (By.ID, "telno")
    _code_locator = (By.ID, "code")
    _next_locator = (By.ID, "next")

    def goto_login(self):
        self.find(self._login_locator).click()
        self.switch_to_window()
        return self

    def login_by_code_fail(self, telno, code):
        self.find(self._telephone_num_locator).send_keys(telno)
        self.find(self._code_locator).send_keys(code)
        self.find(self._next_locator).click()
        return self.switch_to_alert_and_get_text()

