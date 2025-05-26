# test_register.py
import time

import allure
import pytest
from data.data_manager import data_manager

@allure.feature("注册功能")
class TestRegister():
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """自动初始化页面对象，避免传递 main_page 参数"""
        from pages.main_page import MainPage  # 延迟导入避免循环依赖
        self.main_page = MainPage(driver)
        self.driver = driver  # 保留 driver 引用（可选）

    @allure.story("正常注册")
    @allure.title("注册用户")
    @pytest.mark.parametrize(
        'username, password, re_password, nickname, expect',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//register.json")
    )
    def test_01_reg(self, username, password, re_password, nickname,expect):
        reg_page = self.main_page.go_to_reg()
        reg_page.reg_user(username=username, password=password, re_password=re_password, nickname=nickname,expect=expect)
        reg_page.del_cookie()
        time.sleep(2)


if __name__ == '__main__':
    # 运行测试（替代直接调用 pytest）
    pytest.main(["-v", "--alluredir=../report/result"])

