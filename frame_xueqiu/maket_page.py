import importlib

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from learning.frame_xueqiu.base_page import BasePage
from learning.frame_xueqiu.search_page import SearchPage


class MaketPage(BasePage):
    def goto_search(self):
        # self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("step_data.yml", "goto_search")
        return SearchPage(self.driver)
