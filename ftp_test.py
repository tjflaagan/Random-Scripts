import getpass
import ftplib

while 1:
	try:
		user = raw_input("Username: ")
		if user == 'quit':
			break
		mypass = getpass.getpass("Password: ")
		ftp = ftplib.FTP('students.dsu.edu', user, mypass)
		print(ftp.dir())
		ftp.quit()
		print 'Successful Connection'
	except:
		print 'Something failed'
