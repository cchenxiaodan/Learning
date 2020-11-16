import yaml

from learning.frame_xueqiu.main_page import MainPage


def test_frame():
    MainPage().goto_maket().goto_search().search()


def test_step():
    with open("step_data.yml") as f:
        content = yaml.safe_load(f)
    print(content['goto_maket'])
