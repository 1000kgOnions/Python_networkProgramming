##Retrieving email by using IMAP with imaplib
import getpass
import imaplib
import pprint
GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
IMAP_SERVER_PORT='993'
def check_email(username,password):
    mailbox=imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
    mailbox.login(username,password)
    mailbox.select('Inbox')
    tmp,data=mailbox.search(None,'ALL')
    for num in data[0].split():
        tmp,data=mailbox.fetch(num,'(RFC822)')
        print(f'Message: {num}')
        pprint.pprint(data[0][1])
        break
    mailbox.close()
    mailbox.logout()
if _name__=="__main_":
    username=input("Enter your email username: ")
    password = getpass.getpass(prompt='Enter your account password: ')
    check_email(username, password)