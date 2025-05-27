# 说明

这是实验4：`Pytest`（增强版）的代码

项目主要有这5个文件夹组成：`data`，`pages`，`report`，`runner`，`testcases`
`data`文件夹存放了`data_manager.py`文件，它是测试用例加载器文件，采用单例的设计思想。

`pages`文件夹存放了许多如`base_page.py`，`login_page.py`的文件，这些文件与被测的论坛程序的页面一一对应，每一个待测的论坛程序页面都有一份`page.py`文件，存放该页面独有的元素信息，以及操作这些元素的函数。

`report`存放了测试生成结果报告，由`allure`自动生成

`runner`文件夹存放了`run_manager.py`文件，用来配置`allure`的生成参数，以及发送邮件到邮箱的功能

`testcases`文件夹存放了一堆等待被`pytest`进行测试的测试用例对象

整体的设计采用了`PO`的设计思想，主要讲待测试的页面与测试用例进行分离的设计思想