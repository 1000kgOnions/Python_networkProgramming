import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 9999))
data = sk.recv(4096)
print(data.decode('utf-8'))
while True:
    data = input("Nhap choice:")
    sk.send(data.encode("utf-8"))
    s = sk.recv(4096).decode('utf-8')
    print(s)
    if s == 'bye':
        break
sk.close()
