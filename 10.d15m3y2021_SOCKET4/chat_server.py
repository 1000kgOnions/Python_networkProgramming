import socket

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9050))
    sk.listen(10)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Waiting for client")
    try:
        client_sk, addr = sk.accept()
        # print("dia chi client {}".format(addr))
    except socket.error as e:
        # print("ERROR")
        print(e)

    while True:
        data = client_sk.recv(4096)
        print("Tin nhan cua client:", data.decode('utf-8'))
        if data.decode('utf-8') == 'bye':
            # client_sk.send('bye'.encode('utf-8'))
            break
        s = input("Nhap tin nhan: ")
        data = s.encode('utf-8')
        client_sk.send(data)
    sk.close()
    client_sk.close()
