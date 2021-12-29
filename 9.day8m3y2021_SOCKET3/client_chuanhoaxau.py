import socket
if __name__ =='__main__':
        #tạo socket TCP
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.connect(('127.0.0.1',9050))
        while True:
                data=input("nhập chuỗi: ")
                sk.send(data.encode('utf-8'))

                data=sk.recv(4096)
                print("kết quả trả về từ server: {}".format(data.decode('utf-8')))
        sk.close()