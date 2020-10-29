from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from learning.addmember.page.base_page import BasePage


class AddmemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def addmembers(self, uname, uid, uphone):
        self.find(By.ID, "username").send_keys(uname)
        self.find(By.ID, "memberAdd_acctid").send_keys(uid)
        self.find(By.ID, "memberAdd_phone").send_keys(uphone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def getmembers(self):
        memberlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        members = [(element.get_attribute("title")) for element in memberlist]
        print(members)
        return members
