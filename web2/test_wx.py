import pytest

from learning.web2.index_page import IndexPage


class Test_winxin:
    def setup(self):
        self.wx = IndexPage()

    def teardown(self):
        pass

    def test_register(self):
        self.wx.goto_register().register()
