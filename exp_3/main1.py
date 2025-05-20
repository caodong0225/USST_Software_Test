# main1.py
import json
import time
import unittest
from ddt import ddt, data, unpack
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from login import LoginFixture  # 从独立文件导入夹具


@ddt
class ZenTaoBugTest(LoginFixture):
    """主测试类（继承登录夹具）"""
    # 直接从文件加载测试数据（避免类初始化时序问题）
    with open(LoginFixture.TEST_DATA_PATH, encoding="utf-8") as f:
        _test_data = json.load(f)

    @data(*_test_data["bug_cases"])
    @unpack
    def test_create_bug(self, belong_to, belong_module, influenced_version, bug_title,steps):
        """Bug创建测试用例"""
        self.driver.get(self.BASE_URL)  # 回到首页（每次从首页开始）
        # 进入测试模块
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//li[@data-app="qa"]'))
        ).click()

        time.sleep(1)
        # 切换到iframe
        self.driver.switch_to.frame("appIframe-qa")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@data-id="bug"]'))
        ).click()

        # 点击新建Bug按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='btn primary create-bug-btn btn-default']"))
        ).click()

        # 下拉框列表
        self._select_dropdown('//div[@id="zin_bug_create_picker_product"]', '//li[@class="menu-item item"]', belong_to)

        # 选择所属模块
        self._select_dropdown('//div[@id="moduleBox"]', '//li[@class="menu-item item"]', belong_module)

        self._select_dropdown('//div[@data-name="openedBuild"]//div[@class="form-group-wrapper picker-box"]//div',
                              '//li[@class="menu-item item"]', influenced_version)

        # 填写表单操作...
        self._fill_input('//input[@id="zin_bug_create_colorInput"]', bug_title)

        element = self.driver.find_element(
            By.XPATH,
            "//zen-editor"  # 匹配任何标签同时含这两个类
        )
        element.click()
        # 组合键清除内容（比 clear() 更可靠）
        element.send_keys(Keys.CONTROL + 'a')  # 全选
        element.send_keys(Keys.DELETE)  # 删除
        element.send_keys(steps)

        # ...其他字段操作...

        # 提交验证
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-side="bottom"]//button[@class="toolbar-item btn primary"]'))
        ).click()
        success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="alert messager messager-lite success fade-from-top in"]'))
        )
        self.assertIn("保存成功", success_msg.text)

    # 工具方法保持不变
    def _fill_input(self, xpath, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        element.clear()
        element.send_keys(text)

    def _select_dropdown(self, xpath, list_xpath, option_text):
        time.sleep(1)
        # 点击下拉框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()

        # 下拉框列表
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, list_xpath))
        )
        drop_list = self.driver.find_elements(By.XPATH, list_xpath)
        for drop in drop_list:
            if drop.text == option_text:
                drop.click()
                break
        else:
            raise ValueError(f"下拉框中没有找到属于 {option_text} 的选项")


if __name__ == "__main__":
    unittest.main(verbosity=2)
