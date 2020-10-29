from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)

    def find(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element

    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements
