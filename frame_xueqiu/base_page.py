import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from learning.frame_xueqiu.black_deal import black_deal


class BasePage:
    # 设定黑名单
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "ddan"
            caps["appActivity"] = ".main.view.MainActivity"
            caps["appPackage"] = "com.xueqiu.android"
            caps["noReset"] = "True"
            caps["ensureWebviewsHavePages"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

    @black_deal
    def find(self, by, locator=None):
        # 如果传的元素为元组形式，则需要解包
        if locator is None:
            ele = self.driver.find_element(*by)
        else:
            # 如果传的元素有两个
            ele = self.driver.find_element(by, locator)
        return ele

    def parse(self, steps):
        for step in steps:
            if 'click' in step["action"]:
                self.find(step["by"], step["locator"]).click()
            if 'sendkey' in step["action"]:
                self.find(step["by"], step["locator"]).send_keys(step["content"])

    def parse_yaml(self, path, func):
        with open(path, encoding='utf-8') as f:
            datas = yaml.load(f)
        steps = datas[func]
        self.parse(steps)
