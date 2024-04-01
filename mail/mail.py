import smtplib
from email.mime.text import MIMEText

# 设置SMTP服务器和登录信息
smtp_server = 'smtp.office365.com'
smtp_port = 587
email_address = ''
password = ''

# 设置收件人和邮件内容
from_address = email_address
to_address = ''
subject = '邮件主题'
body = '邮件内容'

# 创建一个MIMEText对象
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_address
msg['To'] = to_address

# 连接到SMTP服务器并发送邮件
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # 启动TLS加密
        server.login(from_address, password)  # 登录到SMTP服务器
        server.send_message(msg)  # 发送邮件
except smtplib.SMTPAuthenticationError as e:
    print("SMTPAuthenticationError:", e)
except Exception as e:
    print("Error:", e)