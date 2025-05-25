# conftest.py
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver_path = "D:\\pythonproject\\software_test\\driver\\chromedriver.exe"
    chrome_options = Options()
    chrome_service = Service(driver_path)
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    """自动创建 MainPage 对象"""
    from pages.main_page import MainPage  # 延迟导入避免循环依赖
    return MainPage(driver)
