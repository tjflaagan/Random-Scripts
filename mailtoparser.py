import urllib2
import os
filename = 'emaillst11.txt'
html_content = urllib2.urlopen('PUTURLCONTAININGMAILTOTAGSHERE').read()
l = []
text_file = open(filename, "w")
for item in html_content.split("\n"):
	if "mailto" in item:
		l.append(item.strip() + '\n')

for i in l:
	i = i.split(':', 2)[1]
	i = i.split('"', 2)[0]
	i = i + '\n'
	text_file.write(i)

text_file.close()
print(filename + ' created in ' + os.getcwd())