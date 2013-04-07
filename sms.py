import smtplib
import string

x = 0
TO = raw_input("TO:                 ")
FROM = raw_input("FROM:               ")
text = raw_input("MESSAGE:            ")
NUMBER = raw_input("NUMBER OF MESSAGES: ")
BODY = string.join((
  	"From: %s" % FROM,
		"To: %s" % TO,
		"",
		text
		), "\r\n")
if NUMBER == "":
	while True:
		server = smtplib.SMTP('mail.starick.me', 26)
		server.ehlo()
		server.login("foobar@starick.me","barfoo")
		server.sendmail(FROM, [TO], BODY)
		server.quit()
if NUMBER != "":
	for x in range(x, int(NUMBER)):
		server = smtplib.SMTP('mail.starick.me', 26)
		server.ehlo()
		server.login("foobar@starick.me","barfoo")		
		server.sendmail(FROM, [TO], BODY)
		server.quit()
'''
FIDO:	sms.fido.ca
BELL:	txt.bell.ca
ROGERS:	pcs.rogers.com
TELUS:	mms.telusmobility.com
'''
