from selenium.webdriver.common.by import By

from learning.frame_xueqiu.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        # self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("ali")
        self.parse_yaml('step_data.yml', 'search')
