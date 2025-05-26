import os
import smtplib
import zipfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


class SendEmail:
    def __init__(self,
                 report_dir="../report/html",
                 zip_name="allure_report.zip",
                 sender="jyzxcaodong@163.com",
                 password="EQ5deQhcqZUQMK4g",
                 smtp_server="smtp.163.com",
                 smtp_port=465,
                 recipients=["867137498@qq.com"],
                 subject="自动化测试报告",
                 sender_name="自动化测试平台"):
        """
        :param report_dir: Allure报告目录路径
        :param zip_name: 压缩后的文件名
        :param sender: 发件邮箱
        :param password: 邮箱密码/授权码
        :param smtp_server: SMTP服务器地址
        :param smtp_port: SMTP端口(默认25/SSL用465)
        :param recipients: 收件人列表
        :param subject: 邮件主题
        :param sender_name: 发件人显示名称
        """
        self.report_dir = report_dir
        self.zip_name = zip_name
        self.sender = sender
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.recipients = recipients
        self.subject = subject
        self.sender_name = sender_name

    def zip_report(self):
        """压缩报告目录"""
        with zipfile.ZipFile(self.zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.report_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, self.report_dir)
                    zipf.write(file_path, arcname)
        print(f"报告已压缩至：{self.zip_name}")

    def send(self):
        """发送带附件的邮件"""
        # 创建邮件对象
        msg = MIMEMultipart()
        msg['From'] = f"{Header(self.sender_name, 'utf-8').encode()} <{self.sender}>"
        msg['To'] = ", ".join(self.recipients)
        msg['Subject'] = Header(self.subject, 'utf-8').encode()

        # 添加正文
        text = MIMEText("本次自动化测试已完成，请查看附件中的Allure报告。", 'plain', 'utf-8')
        msg.attach(text)

        # 添加压缩包附件
        with open(self.zip_name, 'rb') as f:
            attachment = MIMEApplication(f.read(), Name=self.zip_name)
        attachment['Content-Disposition'] = f'attachment; filename="{self.zip_name}"'
        msg.attach(attachment)

        # 发送邮件
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender, self.password)
                server.sendmail(self.sender, self.recipients, msg.as_string())
            print("邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败: {str(e)}")
        finally:
            # 清理压缩包
            if os.path.exists(self.zip_name):
                os.remove(self.zip_name)

    def run(self):
        """一键执行压缩+发送"""
        self.zip_report()
        self.send()


if __name__ == "__main__":
    # 发送邮件（使用默认配置）
    email_sender = SendEmail()
    email_sender.run()