from .base_page import BasePage


class UserPage(BasePage):
    follow_ele = '//button[@class="dzq-button _3dGXPdGhdCm1EloEa162Hd false false dzq-button--medium dzq-button--primary"]'
    ignore_ele = '//div[@class="v4vhGsbQwqXTGbkdkYkS4"]'
    chat_ele ='//button[@class="dzq-button _3dGXPdGhdCm1EloEa162Hd dzq-button--medium"]'
    unfollow_ele = '//button[@class="dzq-button _3dGXPdGhdCm1EloEa162Hd false _3iFX-rtIPG-CT2Kt_ADse1 dzq-button--medium dzq-button--primary"]'
    main_page = 'http://localhost'

    def follow(self):
        self.click_element(self.follow_ele)

    def ignore(self):
        self.click_element(self.ignore_ele)

    def go_to_chat(self):
        self.click_element(self.chat_ele)

    def unfollow(self):
        self.click_element(self.unfollow_ele)

    def undo_ignore(self):
        self.click_element(self.ignore_ele)

    def back_to_main(self):
        self.navigate_to(self.main_page)
