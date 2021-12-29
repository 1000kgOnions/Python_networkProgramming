
# soạn thảo email
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

# def send_email(gui,nhan):
#     #tao header
#     msg = MIMEMultipart()
#     msg['From'] = gui
#     msg['To'] = nhan
#     subject = input("Nhap subject: ")
#     msg['Subject'] = subject

#     #tao body
#     part = MIMEText('text', 'plain')
#     message = input("Nhap noi dung thu: ")
#     part.set_payload(message)
#     msg.attach(part)

#     #gui thu tao smtp session
#     session = smtplib.SMTP('aspmx.l.google.com',25)
#     session.ehlo()
#     session.sendmail(gui, nhan, msg)
#     print("email dc gui den {0}".format(nhan))
#     session.quit()

# if __name__=='__main__':
#     gui = input("nhap dia chi gui:")
#     nhan = input("nhap dia chi nhan:")
#     send_email(gui, nhan)
# tienlong6200@gmail.com
# ledang046@gmail.com