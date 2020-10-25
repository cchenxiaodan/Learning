import shelve

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testdemo:
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(Options=Options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_get_cookies(self):
        # 复用时获取cookies
        # cookies=self.driver.get_cookies()
        # print(cookies)

        # 读取cookies
        db = shelve.open("cookies")
        cookies = db["cookies"]
        db.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            "C:/Users/15351/Desktop/data.xls")
        fname = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert fname == 'data.xls'
        time.sleep(3)
