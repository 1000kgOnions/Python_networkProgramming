# soạn thảo email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

def send_email(gui,nhan):
    #tao header
    msg = MIMEMultipart()
    msg['From'] = gui
    msg['To'] = nhan
    subject = input("Nhap subject: ")
    msg['Subject'] = subject

    #tao body
    part = MIMEText('text', 'plain')
    message = input("Nhap noi dung thu: ")
    part.set_payload(message)
    msg.attach(part)

    #gui thu tao smtp session
    session = smtplib.SMTP('smtp.google.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo
    password=getpass.getpass(prompt="Nhap password: ")
    session.login(gui,password)
    session.sendmail(gui, nhan, msg)
    print("email dc gui den {0}".format(nhan))
    session.quit()

if __name__=='__main__':
    gui = input("nhap dia chi gui:")
    nhan = input("nhap dia chi nhan:")
    send_email(gui, nhan)
# tienlong6200@gmail.com
# ledang046@gmail.com
