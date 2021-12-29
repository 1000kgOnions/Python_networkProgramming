import socket
from time import ctime
if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',9050))
    sk.listen(10)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Waiting for client")
    client_sk, addr = sk.accept()
    print("dia chi client {}".format(addr))
    while True:
        # truyen tin thong qua client
        # nhan "time" tu client
        data = client_sk.recv(4096).decode("utf-8")
        if data =='time':
            s = bytes(ctime(),'utf-8')
        else:
            s= 'hi'.encode('utf-8')
        print("server nhan lenh : {}".format(data))
        client_sk.send(s)
        # client_sk.send(bytes(ctime(),'utf-8'))
    sk.close()
    client_sk.close()
