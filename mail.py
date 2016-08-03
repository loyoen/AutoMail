#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
from email.mime.multipart import MIMEMultipart  

sender = 'loyoen@126.com'  
receiver = 'xxx@qq.com'  
subject = '数据库备份'  
smtpserver = 'smtp.126.com'  
username = 'loyoen@126.com'  
password = 'xxx'  
  
#msg = MIMEText('请查看数据库备份','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg = MIMEMultipart('数据库备份')
msg['Subject'] = Header(subject, 'utf-8')  
msg['From'] = 'loyoen@126.com'    
msg['To'] = "xxx@qq.com" 
 
att = MIMEText(open('test.cpp', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="test.cpp"'  
msg.attach(att)  

smtp = smtplib.SMTP()  
smtp.connect('smtp.126.com',25)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit() 
