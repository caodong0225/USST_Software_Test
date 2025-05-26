from .base_page import BasePage


class ReplyPage(BasePage):
    like_ele = '//div[@class="dzq-icon dzq-icon-LikeOutlined"]'
    reply_ele = '//div[@class="_1JR8S859HCIbN9DD7HISTO"]//textarea[@style="height: 125px;"]'
    main_page = 'http://localhost'

    def like(self):
        self.click_element(self.like_ele)

    def reply(self, content):
        self.fill_blank(self.reply_ele, content)

    def back_to_main(self):
        self.navigate_to(self.main_page)
