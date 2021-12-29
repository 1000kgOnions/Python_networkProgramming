# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:04:26 2021

@author: admin
"""

import socket
if __name__=='__main__':
     sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     sk.connect(('127.0.0.1',9000))
     data=sk.recv(1024).decode('utf-8')
     print(data)
     s= input("nhap ")
     sk.send(s.encode('utf-8'))
     while True:
         print(sk.recv(1024).decode('utf-8'))
         if(s=='3'):
             break
         s=input('nhap lai')
         sk.send(s.encode('utf-8'))
     sk.close()