# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : XueqiuTestEngine
@File    : exception.py
@Time    : 2020-04-06  14:51:29
@Author  : indeyo_lin
"""
import logging

logging.basicConfig(level=logging.INFO)

# error_max=10
# error_account=0
# black_list=[
#     (By.ID, "image_cancel"),
#     (By.XPATH, "//*[@text='同意']"),
#     (By.XPATH, "//*[@text='下次再说']")
# ]

def exception_handle(func):
    def magic(*args, **kwargs):
        # 互相调用
        from pages.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance._retry_account = 0
            return result
        except Exception as e:
            if instance._retry_account < instance._retry_max:
                instance._retry_account += 1
                for element in instance._black_list:
                    logging.info(element)
                    elements = instance._driver.find_elements(*element)
                    if len(elements) > 0:
                        elements[0].click()
                        return magic(*args, **kwargs)
            logging.warning("no error is found")
            raise e
    return magic
