import pytest
import yaml

from learning.addmember.page.main_page import MainPage


def data_lode():
    with open("./data.yml") as f:
        data = yaml.safe_load(f)
    return data


class Testadd:
    def setup(self):
        self.add = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize('uname,uid,uphone', data_lode())
    def test_add(self, uname, uid, uphone):
        # uname = "test3"
        # uid = "test3"
        # uphone = "12626000003"
        wx = self.add.goto_addmembers()
        wx.addmembers(uname, uid, uphone)
        assert uname in wx.getmembers()
