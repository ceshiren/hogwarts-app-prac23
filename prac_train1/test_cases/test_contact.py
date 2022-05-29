"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from prac_train1.base.bas_page import BasePage
from prac_train1.utils.contact_info import ContactInfo
from prac_train1.utils.log_util import logger

"""
前提条件：
1、提前注册企业微信管理员帐号
2、手机端安装企业微信
3、企业微信 app 处于登录状态
"""


class TestContact(BasePage):

    def test_addcontact(self):
        """
        通讯录添加成员用例步骤:
            进入【通讯录】页面
            点击【添加成员】
            点击【手动输入添加】
            输入【姓名】【手机号】并点击【保存】
        验证点：
            登录成功提示信息
        """
        name = ContactInfo.get_name()
        phonenum = ContactInfo.get_phonenum()
        # 1. 进入【通讯录】页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 2. 点击【添加成员】
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find("添加成员").click()
        # 3. 点击【手动输入添加】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        # 4. 输入【姓名】
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名' )]/../*[@text='必填']"). \
            send_keys(name)
        # 5. 输入【手机号】
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[contains(@text,"手机" )]/..//android.widget.EditText'). \
            send_keys(phonenum)
        # 6. 点击【保存】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        # time.sleep(2)
        # print(self.driver.page_source)
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # 验证点：登录成功提示信息
        assert result == "添加成功"
