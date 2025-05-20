# login.py
import unittest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginFixture(unittest.TestCase):
    """可复用的登录夹具（跨文件使用）"""

    # 类级配置（子类可覆盖）
    DRIVER_PATH = "D:\\pythonproject\\software_test\\driver\\chromedriver.exe"
    TEST_DATA_PATH = "test_data.json"
    BASE_URL = "http://localhost"

    def setUp(self):
        """每条测试用例前初始化浏览器并登录"""
        chrome_options = webdriver.ChromeOptions()
        chrome_service = webdriver.chrome.service.Service(self.DRIVER_PATH)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

        # 加载登录数据并登录
        with open(self.TEST_DATA_PATH, encoding="utf-8") as f:
            self.test_data = json.load(f)
        self._perform_login()

    def _perform_login(self):
        login_data = self.test_data["login"]
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="account"]'))
        ).send_keys(login_data["username"])
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(login_data["password"])
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="menu"]'))
        )

    def tearDown(self):
        """每条用例后关闭浏览器"""
        self.driver.quit()
        print("\n浏览器已关闭")