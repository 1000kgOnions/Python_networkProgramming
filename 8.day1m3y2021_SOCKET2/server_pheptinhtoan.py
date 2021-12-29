import socket
# """ C1:dùng hàm giống switch case """
# def pheptoan(i):
#         switcher={
#                 '+':int(d[0]) + int(d[1]),
#                 '-':int(d[0]) - int(d[1]),
#                 '*':int(d[0]) * int(d[1]),
#                 '/':int(d[0]) / int(d[1]),
#         }
#         return switcher.get(i,"Nhập phép tính không phù hợp")

# if __name__=='__main__':
#         sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sk.bind(('127.0.0.1',9050))
#         sk.listen(5)
#         sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         client_sk, addr = sk.accept()
#         print("Waiting connection.....")
#         while True:
#                 data = client_sk.recv(256)
#                 d=data.decode('utf-8').split(' ')     #d[0]=a vs d[1]=b vs d[2]=pheptoan
#                 """ C2 """
#                 choices = {'+': int(d[0]) + int(d[1]),
#                 '-': int(d[0]) - int(d[1]),
#                 '*': int(d[0]) * int(d[1]),
#                 '/': int(d[0]) / int(d[1]),}
#                 result = choices.get(d[2],'Nhập phép tính không phù hợp')

#                 # client_sk.send(str(pheptoan(d[2])).encode('utf-8'))   #C1
#                 client_sk.send(str(result).encode('utf-8'))    #C2
#         client_sk.close()
#         sk.close()

""" Thầy chữa """
if __name__ == '__main__':
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind(('127.0.0.1', 9050))
        sk.listen(5)
        sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Waiting connection for client.....")
        client, client_addr = sk.accept()
        print("dia chi client: {}".format(client_addr))
        while True:
                data = client.recv(4096)
                # d[0]=a vs d[1]=b vs d[2]=pheptoan
                d = data.decode('utf-8').split(' ')
                if (d[2] not in ['+','-','*','/']) or ( d[0].isdigit() != True) or ( d[1].isdigit() != True):
                        kq=("Vui long nhap lai phep tinh")
                else:
                        if d[2] == '+':kq = int(d[0]) + int(d[1])
                        if d[2] == '-':kq = int(d[0]) - int(d[1])
                        if d[2] == '*':kq = int(d[0]) * int(d[1])
                        if d[2] == '/':kq = int(d[0]) / int(d[1])

                print("server nhận: {}".format(data))
                client.send(str(kq).encode('utf-8'))
        client.close()
        sk.close()
