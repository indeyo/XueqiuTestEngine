# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : web.py
@Time    : 2020-04-08  16:48:41
@Author  : indeyo_lin
"""
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.web_pages.index import IndexPage


class Web(BasePage):
    _base_url = "https://xueqiu.com/"
    # _driver: webdriver
    _send_text_locator = (By.LINK_TEXT, "发帖")

    # def __init__(self):
    # todo: 这里用init就会报错：AttributeError: 'Web' object has no attribute '_driver'
    def start(self):
        if self._driver is None:
            # chrome --remote-debugging-port=9222
            # 复用已有浏览器
            options = webdriver.ChromeOptions()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)

            self._driver.get(self._base_url)
            self._driver.set_window_size(1500, 1000)
            self._driver.implicitly_wait(10)
        return self

    def start_with_cookies(self):
        if self._driver is None:
            self._driver = webdriver.Chrome()
            # 传入cookies之前要先登录雪球网页。selenium默认域名是data:，cookies中自带域名，
            # 发现当前域名不包含在cookies中时，则cookies设置失败 。
            self._driver.get(self._base_url)

            # 从文件中获取cookies
            # todo: 文件路径写法不够优雅，最好写成相对路径，引用当前项目地址
            with open("D:\project\XueqiuTestEngine\config\cookies.json") as f:
                cookies = json.load(f)
            for cookie in cookies:
                # 由于selenium的cookies不支持expiry，所以需要去掉
                if "expiry" in cookie.keys():
                    # 字典的pop方法可以把字段压出栈
                    cookie.pop("expiry")
                # 传入cookies
                self._driver.add_cookie(cookie)

            self._driver.get(self._base_url)
            self._driver.set_window_size(1500, 1000)
            self._driver.implicitly_wait(10)
        return self

    def index(self):
        return IndexPage(self._driver)

    def save_cookies(self):
        print(self._driver)
        cookies = self._driver.get_cookies()
        # 将cookies保存起来
        with open('D:\project\XueqiuTestEngine\config\cookies.json', 'w') as f:
            json.dump(cookies, f)

    def check_if_login(self):
        return self.find_element_and_get_text(self._send_text_locator)

    def quit(self):
        sleep(20)
        self._driver.quit()
