# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : message.py
@Time    : 2020-04-07  15:13:43
@Author  : indeyo_lin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MessagePage(BasePage):
    _message_list_locator = (By.ID, "title")
    _back_locator = (By.ID, "action_back")

    def get_message_list(self):
        message = self.find_elements_and_get_text(self._message_list_locator)
        self.find(self._back_locator).click()
        return message