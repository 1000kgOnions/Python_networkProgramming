# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:59:32 2021

@author: admin
"""

import socket
import random

if __name__=="__main__":
    
    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',9000))
    sk.listen(5)
    client,addr= sk.accept()
    s='1,love\n2,lotto\n3,quit'
    client.send(s.encode('utf-8'))
    data= client.recv(1024).decode('utf-8')
    while True:
        if data=='1':
            listlove=['trang','hong','anh']
            index= random.randint(0, len(listlove)-1)
            client.send(listlove[index].encode('utf-8'))            
        elif data=='2':            
            index=random.randint(0, 99)
            client.send(str(index).encode('utf-8'))           
        elif data=='3':
            s='bye'
            client.send(s.encode('utf-8'))  
            break
        else:   
            client.send('1,love\n2,lotto\n3,quit'.encode('utf-8'))
        data=client.recv(1024).decode('utf-8')
            
    sk.close()
    client.close()
    
    