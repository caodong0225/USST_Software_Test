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

    @classmethod
    def setUpClass(cls):
        """初始化浏览器并登录"""
        # 初始化浏览器
        chrome_options = webdriver.ChromeOptions()
        chrome_service = webdriver.chrome.service.Service(cls.DRIVER_PATH)
        cls.driver = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options
        )
        cls.driver.get(cls.BASE_URL)
        cls.driver.maximize_window()

        # 加载测试数据
        with open(cls.TEST_DATA_PATH, encoding="utf-8") as f:
            cls.test_data = json.load(f)

        # 执行登录
        cls._perform_login()

    @classmethod
    def _perform_login(cls):
        """具体的登录实现"""
        login_data = cls.test_data["login"]
        WebDriverWait(cls.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="account"]'))
        ).send_keys(login_data["username"])

        cls.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(login_data["password"])
        cls.driver.find_element(By.XPATH, '//button[@id="submit"]').click()

        # 验证登录成功
        WebDriverWait(cls.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="menu"]'))
        )

    @classmethod
    def tearDownClass(cls):
        """清理资源"""
        cls.driver.quit()
        print("\n浏览器已关闭")
