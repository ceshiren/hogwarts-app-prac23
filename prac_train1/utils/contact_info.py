"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from faker import Faker

from prac_train1.utils.log_util import logger


# pip install Faker
# Mock 假数据
class ContactInfo:
    # 定义类方法
    @classmethod
    def get_name(cls):
        name = Faker('zh_CN').name()
        logger.info(f"name: {name}")
        return name

    @classmethod
    def get_phonenum(cls):
        phonenum = Faker('zh_CN').phone_number()
        logger.info(f"phonenum: {phonenum}")
        return phonenum


if __name__ == '__main__':
    ContactInfo.get_name()
    ContactInfo.get_phonenum()
