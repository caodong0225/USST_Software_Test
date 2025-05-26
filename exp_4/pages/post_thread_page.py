from .base_page import BasePage


class PostThreadPage(BasePage):
    title = '//input[@placeholder="标题（可选）"]'
    content = '//pre[@style="padding: 10px 35px;"]'
    post_button = '//div[@class="kgvpHKBNZhZRO3Hc8MT7U"]//button[@class="dzq-button dzq-button--medium dzq-button--primary"]'
    response = '//div[@class="dzq-toast dzq-toast--center is-show dzq-toast__fadeIn""]//span'
    main_page = 'http://localhost'
    post_page = 'http://localhost/thread/post'

    def post_thread(self, title, content):
        if title:
            self.fill_blank(self.title, title)
        if content:
            self.fill_blank(self.content, content)
        self.click_element(self.post_button)
        assert self.assert_post()

    def back_to_main(self):
        self.navigate_to(self.main_page)

    def navigate_to_post(self):
        self.navigate_to(self.post_page)
        return PostThreadPage(self.driver)
