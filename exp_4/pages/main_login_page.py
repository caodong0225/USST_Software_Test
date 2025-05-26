from .base_page import BasePage
from .post_thread_page import PostThreadPage


class MainLoginPage(BasePage):
    publish = '//button[@class="dzq-button _3L8Cr81g2Nv1ZiJx2T1AUb dzq-button--medium dzq-button--primary"]'
    url = "http://localhost/thread/post"
    def go_to_post(self):
        # self.click_element(self.publish)
        self.navigate_to(self.url)
        return PostThreadPage(self.driver)
