# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : app.py
@Time    : 2020-04-06  10:28:10
@Author  : indeyo_lin
"""
from appium import webdriver

from pages.base_page import BasePage
from pages.app_pages.main import MainPage


class App(BasePage):
    _app_package = "com.xueqiu.android"
    _app_activity = ".view.WelcomeActivityAlias"

    def start_app(self):
        if self._driver is None:
            caps = {}
            caps["appPackage"] = self._app_package
            caps["appActivity"] = self._app_activity
            caps["platformName"] = "android"
            # 仅用于写测试用例调试
            caps["noReset"] = True
            caps["dontStopAppOnReset"] = True
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True
            caps["skipLogcatCapture"] = True

            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            # 不需要做appium的初始化，只需要重新启动app
            # todo：什么情况下才会走到这里？前面的caps设置是不是会影响到？
            self._driver.start_activity(self._app_package, self._app_activity)

        return MainPage(self._driver)

    def restart_app(self):
        pass

    def kill_app(self):
        pass
