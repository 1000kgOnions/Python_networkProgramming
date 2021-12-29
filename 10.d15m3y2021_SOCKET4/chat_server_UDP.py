import socket
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.bind(('127.0.0.1', 9050))
    print("listening...on{}".format(sk.getsockname()))

    while True:
        data, addr = sk.recvfrom(1024)
        print("dia chi client {}".format(addr))
        print(data.decode('utf-8'))
        if data.decode('utf-8') == 'bye':
            break
        s = input("Nhap:")
        sk.sendto(s.encode('utf-8'), addr)
        if s == 'bye':
            break

    sk.close()
