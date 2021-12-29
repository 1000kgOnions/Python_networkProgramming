# -*- coding: utf-8 -*-

import socket
if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('127.0.0.1',9050))
    while True:
        data =input('Nhap:')
        sk.send(data.encode('utf-8'))
        if data == 'time':
            print("Time: {}".format(sk.recv(256).decode('utf-8')))
        elif data == 'exit':
            print("EXIT")
            break
        else:
            print("Khong nhan duoc time")
    sk.close()
