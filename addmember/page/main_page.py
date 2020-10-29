import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

from learning.addmember.page.addmember_page import AddmemberPage
from learning.addmember.page.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):

    def goto_addmembers(self):
        # 直接在首页点击添加联系人
        # self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()

        # 先点击通讯录，再添加联系人
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        element: WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()
        return AddmemberPage(self.driver)
