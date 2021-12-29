import socket
import random
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 9999))
sk.listen(10)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_sk, addr = sk.accept()
data = "1.Love\n2.Loto\n3.quit"
client_sk.send(data.encode("utf-8"))
data = client_sk.recv(4096).decode('utf-8')
gai = ["T", "L", "N"]
while True:
    while (data not in ['1', '2', '3']):
        client_sk.send("1.Love\n2.Loto\n3.quit".encode("utf-8"))
    if data == '1':
        i = random.randint(0, gai.__len__()-1)
        client_sk.send(gai[i].encode("utf-8"))
    elif data == '2':
        i = random.randint(0, 99)
        client_sk.send(str(i).encode("utf-8"))
    elif data == '3':
        client_sk.send("bye".encode("utf-8"))
        break
    data = client_sk.recv(4096).decode('utf-8')
client_sk.close()
sk.close()
