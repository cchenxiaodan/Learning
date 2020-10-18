from learning.calculate import Calculate
import pytest


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

    @pytest.mark.parametrize("a,b,expect", [[1, 1, 2], [0.1, 1.7, 1.8], [-3, -23, -26], [0, 333, 333]],
                             ids=["fisrt one", "second one", "third one", "fourth one"])
    def test_add(self, a, b, expect):
        res = self.cal.add(a, b)
        assert res == expect

    @pytest.mark.parametrize("a,b,expect", [[1, 1, 1], [1, 2, 0.5], [10, 0, "error"]], ids=["one", "two", "three"])
    def test_divide(self, a, b, expect):
        res = self.cal.divide(a, b)
        assert res == expect
