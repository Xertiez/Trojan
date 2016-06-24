import os
f = open ('syslog32.txt', 'a')
os.chdir("/")
for dirname, dirnames, filenames in os.walk('.'):
	
	for subdirname in dirname:
		f.write(os.path.join(dirname, subdirname))
	for filename in filenames:
		f.write(os.path.join(dirname, filename))

