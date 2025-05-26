from .base_page import BasePage


class LoginPage(BasePage):
    username = '//input[@placeholder="输入您的用户名"]'
    password = '//input[@placeholder="输入您的登录密码"]'
    login_button = '//div[@class="_1uoYylPL0K32Zg7N_K-K-O"]//button'
    response = '//div[@class="dzq-toast dzq-toast--center is-show dzq-toast__fadeIn"]//span'

    def login_user(self, username, password):
        self.fill_blank(self.username, username)
        self.fill_blank(self.password, password)
        self.click_element(self.login_button)
        res = self.find_element_visible_xpath(self.response).text
        assert res == "登录成功"
