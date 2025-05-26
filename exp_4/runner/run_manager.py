import os
from multiprocessing import Pool

from runner.send_email import SendEmail


class RunManager:
    def __init__(self):
        result_dir = "../report/result"
        if os.path.exists(result_dir):
            for file in os.listdir(result_dir):
                file_path = os.path.join(result_dir, file)
                os.remove(file_path)

    def run_pytest(self, file):
        cmd = f"pytest {os.path.abspath(file)} --alluredir ../report/result"
        os.system(cmd)

    def run_and_create_report(self):
        files = ["../testcases/test_register.py"]
        with Pool(1) as pool:
            pool.map(self.run_pytest, files)
        os.path.abspath(__file__)
        os.system('allure generate --clean ../report/result -o ../report/html')


if __name__ == "__main__":
    RunManager().run_and_create_report()

    # 发送邮件

    # email_sender = SendEmail()
    # email_sender.run()