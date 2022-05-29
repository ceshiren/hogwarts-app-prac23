"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from prac_train1.utils.contact_info import ContactInfo
from prac_train1.utils.log_util import logger

"""
前提条件：
1、提前注册企业微信管理员帐号
2、手机端安装企业微信
3、企业微信 app 处于登录状态
"""


class TestContact:
    implicitly_wait_time = 30

    def setup(self):
        # 资源初始化
        # 打开【企业微信】应用
        caps = {}
        caps["platformName"] = "Android"
        # mac: adb logcat ActivityManager:I | grep "cmp"
        # windows:adb logcat ActivityManager:I | findstr "cmp"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # adb devices
        caps["deviceName"] = "emulator-5554"
        # "True" 是绝对不可以的  要么是"true" 要么是 True
        # 防止清缓存
        caps["noReset"] = "true"
        # 创建driver ,与appium server建立连接，返回一个 session
        # driver 变成self.driver 由局部变量变成实例变量，就可以在其它的方法中引用这个实例变量了
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待是全局的等待方式
        self.driver.implicitly_wait(self.implicitly_wait_time)

    def teardown(self):
        self.driver.quit()

    def swipe_find(self, text, num=3):
        # 自定义滑动查找，
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                element = self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(self.implicitly_wait_time)
                return element
            except:
                logger.info("未找到元素，开始滑动")
                # 获取当前屏幕尺寸
                # 'width', 'height'
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                logger.info(f"当前屏幕的宽：{width}, 高：{height}")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000
                logger.info("开始滑动")
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                self.driver.implicitly_wait(self.implicitly_wait_time)
                raise NoSuchElementException(f"找了{num}次 ，未找到元素{text}")

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
