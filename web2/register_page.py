from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys("chenxiaodan")
        return True
