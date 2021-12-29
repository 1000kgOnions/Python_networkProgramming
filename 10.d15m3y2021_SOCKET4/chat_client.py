import socket
""" client """
if __name__ == '__main__':
    try:
        # tạo socket TCP
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("loi {}".format(e))
    hostname = '127.0.0.1'
    portnumber = 9050
    try:
        sk.connect((hostname, portnumber))
        # sk.close()
    except socket.error as e:
        print("loi {}".format(e))
    while True:
        s = input("nhập tin nhắn: ")
        data = s.encode('utf-8')
        sk.send(data)
        data = sk.recv(4096)
        print(f"Tin nhan cua server: {data.decode('utf-8')}")
        if s == 'bye':
            break
    sk.close()
