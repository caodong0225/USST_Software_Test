from .base_page import BasePage

class MessagePage(BasePage):
    send_button = '//button[@class="dzq-button GqGlJJ3LdVpsiZ59V002d dzq-button--medium dzq-button--primary"]'
    input_box = '//textarea'
    main_page = 'http://localhost'

    def send_text(self,content):
        self.fill_blank(self.input_box,content)
        self.click_element(self.send_button)

    def back_to_main(self):
        self.navigate_to(self.main_page)
