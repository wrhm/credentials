#encryptRaw.py

import sys, os
from crypto import *

if len(sys.argv)!=3:
	print 'Usage: python encryptRaw.py [plaintext.txt] [key]'
	sys.exit()

filename = sys.argv[1]
extension = filename[-3:]

pwMaster = sys.argv[2]

if extension != 'txt':
	print 'Run encryptRaw.py on a text file.'
	sys.exit()

deletionPromptResponse = raw_input('\nFor your security, "%s" will be deleted. Proceed (Y/N)? '%filename)
if 'n' in deletionPromptResponse or 'N' in deletionPromptResponse:
	'Exiting...'
	sys.exit()

f = open(filename)
plain = f.read()
f.close()

secure = encrypt(plain,pwMaster)

f = open('secure.txt','w')
f.write(secure)
f.close()

h = myHash(plain)

f = open('p_hash.txt','w')
f.write(h)
f.close()

os.system('rm %s'%filename)
print '"%s" deleted. Encrypted data stored in "secure.txt".'%filename
print 'You can now run credentials.py.'
