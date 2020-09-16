# # Alt-D gets the browsers address bar from Firefox
import sys
import os
from pathlib import Path
sys.path.append(str(Path.absolute(Path(__file__).resolve().parent.parent) / 'jpSource'))
import jp_stdout
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
from email.mime.text import MIMEText

import mimetypes
from email.message import EmailMessage
import ntpath


destination = 'jpartridge@zoho.com'
subject = 'subject'
# content = 'content'
fullpath = 'c:\\docs\\damon john\\Damon John S&T.est'
print('do we have a log?')
# fullpath = ''
# if len(sys.argv) >= 3:
# destination = [sys.argv[1]]
# subject = sys.argv[2]
    # content = sys.argv[3]
# if len(sys.argv) == 4:
# fullpath = sys.argv[3]
fullpath = 'c:\\docs\\damon john\\Damon John S&T.est'
print(f'fullpath = {fullpath}')
    
SMTPserver = 'smtp.zoho.com'
sender =     'jpartridge@zoho.com'
USERNAME = "jpartridge"
PASSWORD = "T875-1684"

# text_subtype = 'plain'  if error uncomment this *********************************
maintype = 'application'
subtype = 'octet-stream'

try:
    msg = EmailMessage()
    msg['Subject']= subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all
    msg['To'] = destination  # ','.join(destination)
    if fullpath != '':
        with open(fullpath, 'rb') as fp:
                    msg.add_attachment(fp.read(),
                                    maintype=maintype,
                                    subtype=subtype,
                                    filename=ntpath.basename(fullpath))
    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message


