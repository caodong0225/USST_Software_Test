from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 替换为你的驱动地址
driver_path = "D:\\pythonproject\\software_test\\driver\\chromedriver.exe"
chrome_options = Options()
chrome_service = Service(driver_path)

my_username = 'root'
my_password = '123456'
search_nickname = "test3"
disable_reason = "该用户没有缴纳费用"

try:
    # 获取126官网
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    driver.get("http://localhost/admin")
    username_inp = driver.find_element(By.XPATH, '//input[@placeholder="请输入用户名"]')
    password_inp = driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]')
    username_inp.send_keys(my_username)
    password_inp.send_keys(my_password)
    submit_button = driver.find_element(By.XPATH, '//button')
    submit_button.click()
    # 等待页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="menu-demo"]//li')))
    menus = driver.find_elements(By.XPATH, '//ul[@class="menu-demo"]//li')
    # 等待登录成功提示框消失
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//div[@style="top: 20px; z-index: 2000;"]')))
    for menu in menus:
        if menu.text == '用户':
            menu.click()
            break

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@header="用户昵称："]//input')))
    # 查找用户
    find_nickname = driver.find_element(By.XPATH, '//div[@header="用户昵称："]//input')
    find_nickname.send_keys(search_nickname)

    # 进行搜索
    search_button = driver.find_element(By.XPATH, '//button[@class="el-button el-button--primary el-button--medium"]')
    search_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//th[@colspan="1"]//span[@class="el-checkbox__input"]')))
    driver.find_element(By.XPATH, '//th[@colspan="1"]//span[@class="el-checkbox__input"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//main[@class="card-box__main"]//button')))
    driver.find_element(By.XPATH, '//main[@class="card-box__main"]//button').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入禁用理由"]')))
    driver.find_element(By.XPATH, '//input[@placeholder="请输入禁用理由"]').send_keys(disable_reason)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="el-message-box__btns"]//button')))
    for btn in driver.find_elements(By.XPATH,'//div[@class="el-message-box__btns"]//button'):
        if btn.text == '提交':
            btn.click()

    sleep(10)
except Exception as e:
    print(e)
