import shelve

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


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

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1603633010'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635169010, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1603604433,1603604540,1603633010'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'u8znXYUeDaIksqbZGNl0jD8vRfkQj8h9_8aN2yXfnna86QnBiKluKkf1XWojRzffj1N0te5r9Q3fSVrZLUBokWd3IQgKHVou9aAti0Hzi2Mkzx4XFUw5JkM9fCfh07gqAfU8Roau75PNKTp-CJUxk-kM-8GYooLebayAXg3G4Wv-ydbVhdRij7s-aaPTsNwIOlVhisjDaa1ABfEIjuJsSkAgsVX7Sl3lIQn_pa6U6nIvl71QIKWpXY-zVquqmHsxEXbKVqL_ZwUvoljrmq7U_A'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850477665392'},
            {'domain': '.qq.com', 'expiry': 1918048337, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': True,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850477665392'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '28334792813435246'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '8QBeeT10qgSAqVtClx2RuGc-ohxIQFa9k3ym1REv1Vm006gswaml8YJZVj-mLe4F'},
            {'domain': '.qq.com', 'expiry': 1603719972, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.288405627.1603604434'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': True,
             'value': 'ssid=s1335461952'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603635968, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '33hg633'},
            {'domain': '.qq.com', 'expiry': 1666705572, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1850114724.1603604434'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606225574, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1605799349, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': True,
             'value': '000100001927bc6613e2782339430f30b61cf51d69eec26db36940f77f086fa26c747eeeaf110ab70a571fb6'},
            {'domain': '.qq.com', 'expiry': 1605799349, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': True,
             'value': 'o1535190250'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324977166183'},
            {'domain': '.qq.com', 'expiry': 1900081292, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': True, 'value': '1_1535190250'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a333598'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': True, 'value': '1535190250'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '9934421620'},
            {'domain': '.qq.com', 'expiry': 1900081292, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/',
             'secure': True, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '90ae3fb65de7dc210066179411f47982208d685c7cc6221171492598ffeea310'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635140432, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1899476532, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': '93a4046dce69b7dc'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'pxiYSfFmd+'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '6615610368'}]
        db = shelve.open("cookies")
        db["cookies"] = cookies
        db.close()

        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # time.sleep(2)
