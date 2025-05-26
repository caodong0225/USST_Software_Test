from .base_page import BasePage


class RegPage(BasePage):
    username = '//input[@placeholder="输入您的用户名"]'
    password = '//input[@placeholder="输入您的登录密码"]'
    re_password = '//input[@placeholder="确认密码"]'
    nickname = '//input[@placeholder="输入您的昵称"]'
    register_button = '//button[@class="dzq-button _3qtPDEmytvykrslyhEGrDP dzq-button--medium dzq-button--primary"]'
    response = '//div[@class="dzq-toast dzq-toast--center is-show dzq-toast__fadeIn"]//span'

    def reg_user(self, username, password, re_password, nickname, expect):
        self.fill_blank(self.username, username)
        self.fill_blank(self.password, password)
        self.fill_blank(self.re_password, re_password)
        self.fill_blank(self.nickname, nickname)
        self.click_element(self.register_button)
        res = self.find_element_visible_xpath(self.response).text
        assert res == expect
