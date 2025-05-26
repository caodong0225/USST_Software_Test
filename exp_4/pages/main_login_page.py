from .base_page import BasePage
from .post_thread_page import PostThreadPage
from .reply_page import ReplyPage


class MainLoginPage(BasePage):
    publish = '//button[@class="dzq-button _3L8Cr81g2Nv1ZiJx2T1AUb dzq-button--medium dzq-button--primary"]'
    url = "http://localhost/thread/post"
    like_id = "http://localhost/thread/"
    def go_to_post(self):
        # self.click_element(self.publish)
        self.navigate_to(self.url)
        return PostThreadPage(self.driver)

    def like_and_reply(self,id):
        url = self.like_id+str(id)
        self.navigate_to(url)
        assert self.is_404()
        return ReplyPage(self.driver)


