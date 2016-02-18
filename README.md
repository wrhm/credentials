# Credentials

## What is it?
Credentials is a way for Gmail users to securely and locally store sensitive
login information. It uses symmetric private-key encryption to protect your
data, and two-factor authentication to control access.

## Usage
Using Credentials is straightforward:
	- Use encryptRaw.py to encrypt and store login data in secure.txt.
	- Then run credentials.py to access data.

If you are using Credentials for the first time, you will be prompted to do a
couple things:
	- Generate an Application Specific Password (ASP) through your Gmail account
		- Include this and your gmail address in notify.py.
	- Prepare a plaintext file of your credentials
		- Each entry should be on a separate line
		- There should be only spaces separating the data within a line

Example plaintext.txt contents:

	Gmail GmailUsername GmailPassword
	Facebook FacebookUsername FacebookPassword
	Bank BankUsername BankPassword
	OtherSite OtherSiteUsername OtherSitePassword

Once this setup is done, you are ready to run credentials.py. The script
will verify that all necessary files are correctly initialized, and begin the
authentication protocol. You will receive an email with a numerical code that
must be entered to proceed.
	You must then enter the key used to encrypt your data. The script compares a
hash of the original data with a hash of the attempted decryption. If the hashes
differ, the script exits.
	
****IMPORTANT NOTE****
	Keep in mind that, for your security, your plaintext data gets erased as
the encrypted file in generated. If you forget your encryption key, recovering
your data will be extremely difficult.
