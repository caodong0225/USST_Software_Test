# main_page.py
from .base_page import BasePage
from .main_login_page import MainLoginPage
from .post_thread_page import PostThreadPage
from .reg_page import RegPage
from .login_page import LoginPage


class MainPage(BasePage):
    main_page = "http://localhost"
    post_page = 'http://localhost/thread/post'
    register_button = '//button[@class="dzq-button _3jPhsGIYJy2A7HBsyiQbMm _3fiUcQkDdHlW5Q9PLLAd6K dzq-button--medium"]'
    login_button = '//button[@class="dzq-button _3jPhsGIYJy2A7HBsyiQbMm dzq-button--medium dzq-button--primary"]'

    def go_to_reg(self):
        self.navigate_to(self.main_page)
        self.click_element(self.register_button)
        return RegPage(self.driver)

    def go_to_login(self):
        self.navigate_to(self.main_page)
        self.click_element(self.login_button)
        return LoginPage(self.driver)

    def finish_login(self, username, password):
        login = self.go_to_login()
        login.login_user(username=username, password=password)
        return MainLoginPage(self.driver)

    def go_to_post(self):
        self.navigate_to(self.post_page)
        return PostThreadPage(self.driver)

    def is_logged_in(self):
        return self.is_login()
