import time

import pytest
import allure

from data.data_manager import data_manager


@allure.feature("发帖功能")
class TestPost:
    @pytest.fixture(autouse=True)  # 作用域改为整个测试类
    def init_driver(self, driver):
        """初始化 Driver 并登录，整个测试类共享登录状态"""
        from pages.main_page import MainPage
        self.driver = driver

        self.main_page = MainPage(driver)
        if self.main_page.is_logged_in():
            from pages.main_login_page import MainLoginPage
            self.main_login_page = MainLoginPage(self.driver)
            self.post_page = self.main_login_page.go_to_post()
        else:
            self.main_login_page = self.main_page.finish_login('admin', 'Admin123')
            # 登录一次并缓存结果
            self.post_page = self.main_login_page.go_to_post()
        yield

    @allure.story("正常流程发帖")
    @allure.title("登录后发布新帖子")
    @pytest.mark.parametrize(
        'title, content',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//post.json")
    )
    def test_create_post_after_login(self, title, content):
        # 直接使用已初始化的 post_page 对象
        self.post_page.post_thread(title=title, content=content)
        time.sleep(1)
        self.post_page.back_to_main()
        time.sleep(1)

    @allure.story("正常点赞发帖")
    @allure.title("登录后回复新帖子")
    @pytest.mark.parametrize(
        'id, content',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//reply.json")
    )
    def test_like_reply_post(self, id, content):
        reply_page = self.main_login_page.like_and_reply(id=id)
        reply_page.like()
        reply_page.reply(content=content)
        time.sleep(1)
        reply_page.back_to_main()
        time.sleep(1)

    @allure.story("正常关注用户")
    @allure.title("登录后关注用户")
    @pytest.mark.parametrize(
        'id',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//follow.json")
    )
    def test_follow_user(self, id):
        user_page = self.main_login_page.operate_user(id=id)
        user_page.follow()
        time.sleep(1)
        user_page.back_to_main()
        time.sleep(1)

    @allure.story("正常取消关注用户")
    @allure.title("登录后取消关注用户")
    @pytest.mark.parametrize(
        'id',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//unfollow.json")
    )
    def test_unfollow_user(self, id):
        user_page = self.main_login_page.operate_user(id=id)
        user_page.unfollow()
        time.sleep(1)
        user_page.back_to_main()
        time.sleep(1)

    @allure.story("正常屏蔽用户")
    @allure.title("登录后屏蔽用户")
    @pytest.mark.parametrize(
        'id',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//ignore.json")
    )
    def test_ignore_user(self, id):
        user_page = self.main_login_page.operate_user(id=id)
        user_page.ignore()
        time.sleep(1)
        user_page.back_to_main()
        time.sleep(1)

    @allure.story("正常取消屏蔽用户")
    @allure.title("登录后取消屏蔽用户")
    @pytest.mark.parametrize(
        'id',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//undo_ignore.json")
    )
    def test_undo_ignore_user(self, id):
        user_page = self.main_login_page.operate_user(id=id)
        user_page.undo_ignore()
        time.sleep(1)
        user_page.back_to_main()
        time.sleep(1)

    @allure.story("正常取消屏蔽用户")
    @allure.title("登录后取消屏蔽用户")
    @pytest.mark.parametrize(
        'id, message',
        data_manager.get_data_json("D://pythonproject//software_test//exp_4//send_message.json")
    )
    def test_send_message(self, id, message):
        message_page = self.main_login_page.send_message(id)
        message_page.send_text(content=message)
        time.sleep(1)
        message_page.back_to_main()
        time.sleep(1)
