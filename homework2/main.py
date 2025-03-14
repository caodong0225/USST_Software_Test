import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 替换为你的驱动地址
driver_path = "D:\pythonproject\software_test\driver\chromedriver.exe"
chrome_options = Options()
chrome_service = Service(driver_path)
file = open("./res.txt","a+")

try:
    # 获取126官网
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    # 设置driver路径
    driver.get('https://www.jd.com/')
    sleep(1)
    appliance = driver.find_element(By.XPATH, "//ul[@class='JS_navCtn cate_menu']/li[@data-index='1']")
    actions = ActionChains(driver)
    actions.move_to_element(appliance).perform()
    sleep(2)
    titles = driver.find_elements(By.XPATH, "//div[@id='cate_item1']/div[@class='cate_part_col1']/div[@class='cate_channel']/a[@class='cate_channel_lk']/span[@class='cate_detail_tit_content']")
    for title in titles:
        file.write(title.text)
        file.write(" ")
    elements = driver.find_elements(By.XPATH, "//div[@id='cate_item1']/div[@class='cate_part_col1']/div[@class='cate_detail']/*/*/*/span[@class='cate_detail_tit_content']")
    for element in elements:
        file.write(element.text)
        file.write(" ")

    time.sleep(10)
    file.close()
except:
    pass
