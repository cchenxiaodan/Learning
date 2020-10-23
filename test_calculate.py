from learning.calculate import Calculate
import pytest
import yaml


def get_datas(mudle, content):
    with open('./calculate_date.yml') as f:
        data = yaml.safe_load(f)
    add_datas = data[mudle][content]
    return add_datas

class Testcalculate:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    def setup_class(self):
        print("用例开始")
        self.cal = Calculate()

    def teardown_class(self):
        print("用例结束")

    @pytest.fixture()
    def fix(self):
        print("fix开始")
        yield
        print("fix结束")

    @pytest.mark.parametrize('a,b,expect', get_datas('add', 'datas'), ids=(get_datas('add', 'ids')))
    def test_add(self, fix, a, b, expect):
        res = self.cal.add(a, b)
        assert res == expect

    @pytest.mark.hhh
    @pytest.mark.parametrize("a,b,expect", get_datas('div', 'datas'), ids=(get_datas('div', 'ids')))
    def test_divide(self, a, b, expect):
        try:
            res = self.cal.divide(a, b)
        except ZeroDivisionError:
            print("除数为0")
        # if b==0:
        #     with pytest.raises(ZeroDivisionError):
        #         self.cal.divide(a,b)
        # else:
        #     res=self.cal.divide(a,b)
        #     assert round(res,2)==expect
