#!/usr/bin/python

print ("lancement pythonmail")

#import smtplib
# 
#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login("nabilcasablanca1982@gmail.com", "casablanca1982")
# 
#msg = "ISMAIL test!"
#server.sendmail("nabilcasablanca1982@gmail.com", "nabilcasablanca1982@gmail.com", msg)
#server.quit()

#import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
# 
# 
#fromaddr = "nabilcasablanca1982@gmail.com"
#toaddr = "nabilcasablanca1982@gmail.com"
#msg = MIMEMultipart()
#msg['From'] = fromaddr
#msg['To'] = toaddr
#msg['Subject'] = "ISMAIL"
# 
#body = "tjs ismail"
#msg.attach(MIMEText(body, 'plain'))
# 
#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login(fromaddr, "casablanca1982")
#text = msg.as_string()
#server.sendmail(fromaddr, toaddr, text)
#server.quit()

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "nabilcasablanca1982@gmail.com"
toaddr = "nabilcasablanca1982@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ISAMIL PJ"
 
body = "ismail pj text"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "C04.pdf"
attachment = open("/home/m2i/Bureau/C04.pdf", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "casablanca1982")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
