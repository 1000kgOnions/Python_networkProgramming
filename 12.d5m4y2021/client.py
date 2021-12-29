import socket
host = '127.0.0.1'
port = 9050


def receive_msg(sk):
    data = bytearray()
    msg = ""
    while not msg:
        b = sk.recv(1024)
        if not b:
            raise ConnectionError()
        data = data + b
        if b'\0' in b:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg


def create_msg(msg):
    msg = msg + '\0'
    return msg.encode('utf-8')


def send_msg(sk, msg):
    data = create_msg(msg)
    sk.sendall(data)


if __name__ == '__main__':
    while True:
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.connect((host, port))
            data = input("Nhap:")
            if data == "exit":
                break
            send_msg(sk, data)
            print("client gui: {}".format(data))
            data = receive_msg(sk)
            print("server gui: {}".format(data))
        except ConnectionError:
            print("Error")
        finally:
            print("Dong ket noi client")
            sk.close()
