# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : base_page.py
@Time    : 2020-04-06  10:28:01
@Author  : indeyo_lin
"""
import logging
from time import sleep

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.exception import exception_handle

logging.basicConfig(level=logging.INFO)


class BasePage:
    _driver: WebDriver
    _retry_max = 10
    _retry_account = 0
    _black_list = [
        (By.ID, "image_cancel"),
        (By.XPATH, "//*[@text='同意']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='allow']")
    ]
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @exception_handle
    def find(self, locator, key=None):
        # todo：logging改成装饰器
        logging.info(locator)
        logging.info(key)
        if not isinstance(locator, tuple):
            locator = (locator, key)
        # todo：显示等待改写成装饰器
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self._driver.find_element(*locator)
        # if isinstance(locator, tuple):
        #     return self._driver.find_element(*locator)
        # else:
        #     return self._driver.find_element(locator, key)

    def find_by_text(self, text):
        return self.find(By.XPATH, '//*[@text="%s"]' % text)

    @exception_handle
    def find_elements_and_get_text(self, locator, key=None):
        if not isinstance(locator, tuple):
            locator = (locator, key)
        WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        elements = []
        # 获取搜索结果的文本信息，并放进数组里
        for element in self._driver.find_elements(*locator):
            elements.append(element.text)
        return elements

    def find_element_and_get_text(self, locator, key=None):
        return self.find(locator, key).text

    def switch_to_window(self):
        windows = self._driver.window_handles
        self._driver.switch_to.window(windows[-1])

    def switch_to_alert_and_get_text(self):
        # 等待弹窗出现
        WebDriverWait(self._driver, 10).until(expected_conditions.alert_is_present())
        # 切换到弹窗
        alert = self._driver.switch_to.alert
        # 保存弹簧内容，用于断言
        text = alert.text
        # 点击弹窗 确认 按钮
        alert.accept()
        return text

    def quit(self):
        sleep(15)
        self._driver.quit()