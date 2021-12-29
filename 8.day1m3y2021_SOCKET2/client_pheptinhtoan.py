import socket
""" client """
# if __name__ =='__main__':
#         #tạo socket TCP
#         sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sk.connect(('127.0.0.1',9050))

#         a=input("nhap so thu 1:")
#         b=input("nhap so thu 2:")
#         c=input("nhap phep tinh:")
#         data= a+ ',' +b+ ',' + c  #gui a,b,pheptinh

#         sk.send(data.encode('utf-8'))
#         data = sk.recv(256)
#         print("Ket qua: {}".format(data))

#         sk.close()

""" Thầy chữa """
if __name__ =='__main__':
        #tạo socket TCP
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('127.0.0.1',9050))
        while True:
                data=input("nhập phép toán: ")
                sk.send(data.encode('utf-8'))
                data=sk.recv(4096)
                print("kết quả trả về từ server: {}".format(data))
        sk.close()


