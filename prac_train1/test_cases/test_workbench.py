"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium import webdriver


class TestWorkbench:
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

    def test_daka(self):
        """
        进入【工作台】页面
        点击【打卡】
        选择【外出打卡】tab
        点击【第 N 次打卡】
        验证点：提示【外出打卡成功】
        :return:
        """
        pass
