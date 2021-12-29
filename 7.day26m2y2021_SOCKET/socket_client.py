import socket
""" client """
if __name__ =='__main__':
    try:
        #tạo socket TCP
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("loi {}".format(e))

    print("da tao socket")
    hostname = '127.0.0.1'
    portnumber = 9050
    try:
        sk.connect((hostname,portnumber))
        print("da ket noi den {}".format((hostname,portnumber)))
        #sk.close()
    except socket.error as e:
        print("loi {}".format(e))
    while True:
        data=input("Nhap lenh:")
        sk.send(data.encode('utf-8'))
        data = sk.recv(4096)
        print("client nhan: {}".format(data.decode('utf-8')))
    sk.close()





