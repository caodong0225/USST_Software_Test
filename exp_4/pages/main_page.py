# main_page.py
from .base_page import BasePage
from .reg_page import RegPage
from .login_page import LoginPage

class MainPage(BasePage):

    main_page = "http://localhost"

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
