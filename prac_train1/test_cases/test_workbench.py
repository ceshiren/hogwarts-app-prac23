"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from prac_train1.base.bas_page import BasePage


class TestWorkbench(BasePage):

    def test_daka(self):
        """
        进入【工作台】页面
        点击【打卡】
        选择【外出打卡】tab
        点击【第 N 次打卡】
        验证点：提示【外出打卡成功】
        :return:
        """
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='工作台']").click()
        self.swipe_find("打卡").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, '次外出')]").click()
        # 断言 assert  find ...最后一步，进行倒数第二步的验证
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='外出打卡成功']")
