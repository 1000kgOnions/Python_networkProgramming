# -*- coding: utf-8 -*-

import socket
from time import ctime
if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',9050))
    sk.listen(5)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    print("waiting connection...")
    client_sk, client_addr = sk.accept()
    while True:
        data = client_sk.recv(256)
        if data.decode('utf-8')== 'exit':
            break
        if data.decode('utf-8') != "time":
            print("Khong dung lenh")
        else:
            client_sk.send(bytes(ctime(),'utf-8'))
    client_sk.close()
    sk.close()