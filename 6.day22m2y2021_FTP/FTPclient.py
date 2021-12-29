import ftplib

def listLineCallback(line):
    msg = "** %s*" % line
    print(msg)

if __name__ == '__main__':
    ftp = ftplib.FTP('ftp.ibiblio.org')
    # ftp = ftplib.FTP(host='', user='', passwd='', acct='', timeout=None, source_address=None)
    print(ftp.getwelcome())  #gửi từ sv khi cli kết nối
    """ login, hienthithumuc(dir/nlst) """
    try:
        ftp.login()
        # file = []
        # ftp.dir(file.append)
        # print(file)
        print(ftp.pwd())  # hiện thư mục hiện thời
        d = ftp.nlst('/') # hiển thị tên file/thư mục
        d.sort()
        print('Tong so file:', len(d))
        for i in d:
            print(i)

        # A cho ascii mode
        ftp.sendcmd('TYPE I')
        filename = "README"
        filesize = ftp.size(filename)
        print(f"Kich thuoc file {filename}:", filesize)

        """ chuyen vao trong thu muc pub xem co gi """
        # C1: từ thư mục gốc
        c1 = ftp.nlst('/pub')
        c1.sort()
        print('Tong so file c1:', len(c1))
        for i in c1:
            print(i)

        # C2: sử dụng cwd  /cwd để đổi thư mục
        # ftp.cwd('pub')
        # c2 = ftp.nlst('')
        # c2.sort()
        # print('Tong so file c2:',len(c2))
        # for i in c2:
        #     print(i)

        # C3:sudung retrlines
        # print(ftp.retrlines('LIST',listLineCallback(ftp.cwd('pub'))))

        """ download file readme """
        # ftp.cwd('/')   #Nếu truy cập thư mục = c2,c3 thì dùng thêm dòng này
        fp = open('README', 'w')
        down = ftp.retrlines('RETR '+'README', fp.write)
        # neu khong hien Error thi la download thanh cong
        if not down.startswith('226 Transfer complete'):
            print('Error')
        else:print('Download complete')
        """ upload file (phai co quyen) """
        # ftp.login('username','password')
        # f=open('ten file','rb')
        # up=ftp.storlines('STOR ','ten file', f)
        # #neu khong hien Error thi la upload thanh cong
        # if not up.startswith('226 Transfer Complete'):
        #     print('Error')

        ftp.quit()
    except ftplib.all_errors as e:
        print("Errorrr:", e)
