import pytest
import yaml
import allure


@allure.feature("数据加载")
def get_datas(mudle, content):
    with open('calculate_date.yml') as f:
        data = yaml.safe_load(f)
    add_datas = data[mudle][content]
    return add_datas


@allure.feature("计算器")
class Testcalculate:
    # def setup(self):
    #     print("开始计算")
    #
    # def teardown(self):
    #     print("计算结束")
    #
    # def setup_class(self):
    #     print("用例开始")
    #     self.cal = Calculate()
    #
    # def teardown_class(self):
    #     print("用例结束")

    @allure.story("加法")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas('add', 'datas'), ids=(get_datas('add', 'ids')))
    def test_add(self, fix, a, b, expect):
        with allure.step("加法计算"):
            res = fix.add(a, b)
        assert round(res, 2) == expect

    @allure.story("除法")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_datas('div', 'datas'), ids=(get_datas('div', 'ids')))
    def test_divide(self, fix, a, b, expect):
        try:
            res = fix.divide(a, b)
        except ZeroDivisionError:
            print("除数为0")
        # if b==0:
        #     with pytest.raises(ZeroDivisionError):
        #         self.cal.divide(a,b)
        # else:
        #     res=self.cal.divide(a,b)
        #     assert round(res,2)==expect

    @allure.story("乘法")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_datas('mul', 'datas'), ids=get_datas('mul', 'ids'))
    def test_mul(self, fix, a, b, expect):
        res = fix.mul(a, b)
        assert res == expect

    @allure.story("减法")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_datas('sub', 'datas'), ids=get_datas('sub', 'ids'))
    def test_sub(self, fix, a, b, expect):
        res = fix.sub(a, b)
        assert res == expect

        allure.attach.file("文本", "name", attachment_type=allure.attachment_type.TEXT)
