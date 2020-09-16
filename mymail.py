import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

myserver = 'smtp.zoho.com'
file = 'c:\\docs\damon john\\damon john s&t.est'
username='jpartridge'
password='T875-1684'
send_from = 'jpartridge@zoho.com'
send_to = 'jpartridge@zoho.com,'
# Cc = 'recipient'
msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = send_to
# msg['Cc'] = Cc
msg['Date'] = formatdate(localtime = True)
msg['Subject'] = 'subject'
port = '465'
server = smtplib.SMTP(myserver, port)

fp = open(file, 'rb')
part = MIMEBase('application','octet-stream')
part.set_payload(fp.read())
fp.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=file)
msg.attach(part)
smtp = smtplib.SMTP(myserver, port)
smtp.ehlo()
smtp.starttls()
smtp.login(username,password)
smtp.sendmail(send_from, send_to.split(',') + msg['Cc'].split(','), msg.as_string())
smtp.quit()