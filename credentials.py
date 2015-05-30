#credentials.py

from random import randint
from crypto import *
import os, sys, string

if len(sys.argv)!=2 or sys.argv[1]!='secure.txt':
	print 'Usage: python credentials.py secure.txt'
        sys.exit()

secureFilename = sys.argv[1]

try:
    f = open('secure.txt','r')
except:
    print 'Run "python encryptRaw.py" to produce "secure.txt"'
    sys.exit()

#Generate and validate a random number
r = randint(10**5,10**6)
f = open('toSend.txt','w')
f.write('credentials.py Login\n')
f.write(str(r))
f.close()
print '\nSending validation code...\n'
os.system('python notify.py')
os.system('rm toSend.txt')

f = open('send_status.txt','r')
QUIT = 'fail' in f.read()
f.close()
os.system('rm send_status.txt')

if QUIT:
    print 'Please edit "notify.py" to have your gmail address and ASP.'
    sys.exit()

codeGuess = None
while codeGuess != str(r):
	if codeGuess != None:
		print '\nCode incorrect.'
	codeGuess = raw_input('code: ')

print '\nYou\'re in!'

pwMaster = raw_input('Decryption key: ')

f = open(secureFilename,'r')
secure = f.read()
f.close()

data = decrypt(secure,pwMaster)

d_hash = myHash(data)

hf = open('p_hash.txt','r')
s_hash = hf.read()
hf.close()

if d_hash!=s_hash:
	print 'Hashes unequal. Exiting...'
	sys.exit()

print 'Hashes match!'

creds = data.split()

found = False
while not found:
	print '\nWhat site do you need to log into?\n'
	site = raw_input('Site: ')
	print '\nCredentials matching "%s":'%site
	for i in xrange(0,len(creds)-2,3):
		if string.lower(site) in string.lower(creds[i]):
			found = True
			print '      Site: %s'%creds[i]
			print '  Username: %s'%creds[i+1]
			print '  Password: %s\n'%creds[i+2]
	if not found:
		print '\tSorry, no entry matching \"%s\" found.\n'%site
	response = string.lower(raw_input('Would you like to view more credentials (Y/N)? '))
	if 'y' in response:
		found = False

os.system('clear')
print 'Access closed.'
