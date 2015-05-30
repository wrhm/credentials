#crypto.py

import string
import hashlib

alpha = "\n"
for i in xrange(32,127):
	alpha += chr(i)

def encrypt(s,key):
	result = ''
	for i in xrange(len(s)):
		strInd = alpha.index(s[i])
		keyInd = alpha.index(key[i%len(key)])
		result += alpha[(strInd+keyInd)%len(alpha)]
	return result

def decrypt(s,key):
	result = ''
	for i in xrange(len(s)):
		strInd = alpha.index(s[i])
		keyInd = alpha.index(key[i%len(key)])
		result += alpha[(strInd+len(alpha)-keyInd)%len(alpha)]
	return result

def myHash(s):
	m = hashlib.md5()
	m.update(s)
	return m.digest()