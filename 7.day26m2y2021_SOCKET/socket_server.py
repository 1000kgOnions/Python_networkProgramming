import socket

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    sk.bind(('127.0.0.1',9050))
    sk.listen(10)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Waiting for client")
    while True:
        client_sk, addr = sk.accept()
        print("dia chi client {}".format(addr))

        # truyen tin thong qua client
        # nhan "hello" tu client
        data = client_sk.recv(4096)
        print("server nhan: {}".format(data))
        data = 'server gui lai'
        client_sk.send(data.encode('utf-8'))
    sk.close()
    client_sk.close()