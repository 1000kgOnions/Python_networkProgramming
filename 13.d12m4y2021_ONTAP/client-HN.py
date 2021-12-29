import socket
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('127.0.0.1', 6969))
    print(sk.recv(1024).decode())
    data = input()
    sk.send(data.encode('utf-8'))
    while True:
        print(sk.recv(1024).decode())
        if(data == '3'):
          break
        data = input()
        sk.send(data.encode('utf-8'))
    sk.close()
