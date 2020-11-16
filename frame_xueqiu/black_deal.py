import allure


def black_deal(func):
    def wrapper(*args, **kwargs):
        from learning.frame_xueqiu.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # 遍历查找黑名单的元素是存在
            instance.driver.save_screenshot('longin.png')
            with open("longin.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
