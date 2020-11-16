import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from learning.frame_xueqiu.base_page import BasePage
from learning.frame_xueqiu.maket_page import MaketPage


class MainPage(BasePage):

    def goto_maket(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.parse_yaml("step_data.yml", 'goto_maket')

        return MaketPage(self.driver)
