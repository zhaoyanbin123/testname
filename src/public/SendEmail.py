# coding=utf-8
import smtplib
import getData
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from config import constants

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def SendReport_Email():
    # 输入Email地址和口令:
    from_addr = getData.getValue().get("from_addr")
    password = getData.getValue().get("password")
    # 输入SMTP服务器地址:
    smtp_server = getData.getValue().get("smtp_server")
    # 输入收件人地址:
    to_addr = getData.getValue().get("to_addr")
    # 如名字所示Multipart就是分多个部分
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'自动化执行者 <%s>' % from_addr)
    msg['To'] = _format_addr(u'收件人 <%s>' % to_addr)
    msg['Subject'] = Header(u'UI自动化测试结果', 'utf-8').encode()
    #---这是文字部分---
    part = MIMEText("This is test report")
    msg.attach(part)
    #---这是附件部分---
    part = MIMEApplication(open(constants.email_path, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="Report.html")
    msg.attach(part)
    s = smtplib.SMTP(smtp_server, timeout=30)  #连接smtp邮件服务器,端口默认是25
    s.login(from_addr, password)  # 登陆服务器
    s.sendmail(from_addr, to_addr, msg.as_string())  #发送邮件
    s.close()

if __name__ == "__main__":
    SendReport_Email()   
    


