#notify.py
#http://stackoverflow.com/questions/6270782/sending-email-with-python

import smtplib, sys

'''
 - Set USERNAME to your gmail address, without the '@gmail.com'.
 - Set PASSWORD to an Application Specific Password linked to
your account.
 - Make sure each of these is in quotes. Example:
    USERNAME = '____'
    PASSWORD = '____'
'''

USERNAME = None
PASSWORD = None

SENDER = '%s@gmail.com'%USERNAME
RECIPIENT = SENDER

f = open('toSend.txt','r')
[SUBJECT,TEXT] = f.read().split('\n')
f.close()

msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (SENDER, RECIPIENT, SUBJECT, TEXT)

f = open('send_status.txt','w')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
try:
    server.login(USERNAME,PASSWORD)
except:
    f.write('failed')
    sys.exit()
server.sendmail(SENDER,[RECIPIENT],msg)
server.quit()
f.close()
