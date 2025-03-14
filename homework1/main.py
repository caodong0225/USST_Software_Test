import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 替换为你的驱动地址
driver_path = "D:\pythonproject\software_test\driver\chromedriver.exe"
chrome_options = Options()
chrome_service = Service(driver_path)

my_name = "xxxxx"  # 替换为我的用户名
my_password = "xxxxx" # 替换为我的密码

try:
    # 获取126官网
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    # 设置driver路径
    driver.get('https://126.com/#!/hisx_mbdx')
    sleep(1)
    # 切换iframe
    driver.switch_to.frame(0)
    # 输入用户名
    name_input = driver.find_element(By.XPATH, "//input[@name='email']")
    name_input.send_keys(my_name)
    # 输入密码
    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(my_password)
    # 勾选记住我
    remember_input = driver.find_element(By.XPATH, "//input[@name='un-login']")
    remember_input.click()
    login_button = driver.find_element(By.XPATH, "//a[@id='dologin']")
    login_button.click()
    time.sleep(10)
except:
    pass
