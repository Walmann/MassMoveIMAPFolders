import imaplib
import json
import re

settings = json.load(open("myIMAPlogin.json", "r"))

# Connect to the IMAP server
MailObject = imaplib.IMAP4_SSL(settings["IMAPserver"])

# Login to the server
MailObject.login(settings["email"],settings["password"])

response_code, response = MailObject.list(pattern="\"INBOX 1*\"", )

for mailbox in response:
    currentFolder = mailbox.decode().split('"')[3]
    currentFolder = f"\"{currentFolder}\""
    temp0 = MailObject.unsubscribe(currentFolder)
    temp1 = MailObject.lsub(currentFolder)
    temp2 = MailObject.delete(currentFolder)
    print(currentFolder)


print()

MailObject.close()
MailObject.logout()