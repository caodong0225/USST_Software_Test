from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage():
    user_info = '//div[@class="dzq-dropdown"]'
    success_info = '//div[@class="_34kcWYQLB3ftXDR3FgEWAk"]'
    _404 = '//img[@class="_26tKvvzLDZVTZTSvKQx3x5"]'
    not_found = '//div[@class="dzq-toast dzq-toast--center is-show dzq-toast__fadeIn"]'

    def __init__(self, driver):  # 通过构造函数接收 driver
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # 打开指定 URL
    def open(self, url):
        self.driver.get(url)

    # 定位元素（XPath）
    def find_element_xpath(self, target):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, target)))

    def find_element_visible_xpath(self, target):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, target)))

    def click_element(self, target):
        self.find_element_xpath(target).click()

    def fill_blank(self, target, value):
        self.find_element_xpath(target).send_keys(value)

    def navigate_to(self, url):
        time.sleep(2)
        self.driver.get(url)

    def del_cookie(self):
        self.driver.delete_all_cookies()

    def assert_post(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.success_info)))
            return True
        except:
            return False

    def is_login(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.user_info)))
            return True
        except:
            return False

    def is_404(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self._404)))
            return False
        except:
            return True

    def is_not_found(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.not_found)))
            return False
        except:
            return True
