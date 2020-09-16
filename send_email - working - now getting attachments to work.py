# # Alt-D gets the browsers address bar from Firefox
# import sys
# import os
# import sys
# from pathlib import Path
# sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
# import jp_stdout
# print('do we have a log?')
# # import re

# destination = [sys.argv[1]]
# subject = sys.argv[2]
# content = sys.argv[3]

# SMTPserver = 'smtp.zoho.com'
# sender =     'jpartridge@zoho.com'
# USERNAME = "jpartridge"
# PASSWORD = "T875-1684"

# # typical values for text_subtype are plain, html, xml
# text_subtype = 'plain'


# from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# # from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# # old version
# # from email.MIMEText import MIMEText
# from email.mime.text import MIMEText

# try:
#     msg = MIMEText(content, text_subtype)
#     msg['Subject']= subject
#     msg['From']   = sender # some SMTP servers will do this automatically, not all
#     msg['To'] = ','.join(destination)

#     conn = SMTP(SMTPserver)
#     conn.set_debuglevel(False)
#     conn.login(USERNAME, PASSWORD)
#     try:
#         conn.sendmail(sender, destination, msg.as_string())
#     finally:
#         conn.quit()

# except:
#     sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message



# import smtplib
# from os.path import basename
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import COMMASPACE, formatdate
# import sys
# from pathlib import Path
# sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
# import jp_stdout


# destination = [sys.argv[1]]
# subject = sys.argv[2]
# content = sys.argv[3]
# if len(sys.argv) == 5:
#     attachment = sys.argv[4]

# SMTPserver = 'smtp.zoho.com'
# sender =     'jpartridge@zoho.com'
# USERNAME =   'jpartridge'
# PASSWORD =   'T875-1684'



# def send_mail(send_from, send_to, subject, text, files=None,
#               server="127.0.0.1"):
#     assert isinstance(send_to, list)

#     msg = MIMEMultipart()
#     msg['From'] = sender
#     msg['To'] = sender
#     msg['Date'] = formatdate(localtime=True)
#     msg['Subject'] = subject

#     msg.attach(MIMEText(text))

#     for f in files or []:
#         with open(f, "rb") as fil:
#             part = MIMEApplication(
#                 fil.read(),
#                 Name=basename(f)
#             )
#         # After the file is closed
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
#         msg.attach(part)


#     smtp = smtplib.SMTP(server)
#     smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.close()

#     send_mail(sender, sender, 'subject', 'text')
#     print('mail sent')

import sys
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
import jp_stdout
print('do we have a log?')



SMTPserver = 'smtp.zoho.com'                     # 'smtp.att.yahoo.com'
sender =     'jpartridge@zoho.com'          # 'me@my_email_domain.net'
destination = ['jpartridge@zoho.com']       #  ['recipient@her_email_domain.com']

# USERNAME = "USER_NAME_FOR_INTERNET_SERVICE_PROVIDER"
# PASSWORD = "PASSWORD_INTERNET_SERVICE_PROVIDER"
USERNAME =   'jpartridge'
PASSWORD =   'T875-1684'

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


content="""\
Test message
"""

subject="Sent from Python"

import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message