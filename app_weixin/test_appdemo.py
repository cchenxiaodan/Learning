# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "ddan"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["appPackage"] = "com.tencent.wework"
        caps["noReset"] = "True"
        caps["ensureWebviewsHavePages"] = True
        # 增加setting设置，减少动态加载时间
        caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_demo(self):
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()

        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[13]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        el2.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, \
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                                 '.scrollIntoView(new UiSelector()' \
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        # time.sleep(3)，由于不用driver的元素查找方式，因此无法适用隐式等待，可用强制或显示等待
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        # 通过page_source判断元素是否存在
        assert "外出打卡成功" in self.driver.page_source

    def teardowm(self):
        self.driver.quit()
