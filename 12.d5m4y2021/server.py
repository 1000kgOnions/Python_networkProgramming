import socket
import threading
host = '127.0.0.1'
port = 9050


def create_socket(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind((host, port))
    sk.listen(10)
    return sk


def receive_msg(sk):
    data = bytearray()
    msg = ""
    while not msg:
        b = sk.recv(1024)
        if not b:
            raise ConnectionError()
        data = data + b
        if b'\0' in b:
            msg = data.rstrip(b'\0') #rstrip(key):xóa ký tự key cuối chuỗi
    msg = msg.decode('utf-8')
    return msg


def create_msg(msg):
    msg = msg + '\0'
    return msg.encode('utf-8')


def send_msg(sk, msg):
    data = create_msg(msg)
    sk.sendall(data)


def process_client(sk, addr):
    try:
        msg = receive_msg(sk)
        msg = "{}:{}".format(addr, msg)
        print(msg)
        s=input("Server nhap:")
        send_msg(sk, s)
    except ConnectionError:
        print("Lõi")
    finally:
        print("Dong ket noi")
        sk.close()


if __name__ == '__main__':
    sk1 = create_socket(host, port)
    addr = sk1.getsockname()
    print("Dia chi cuc bo: {}\n".format(addr))
    # while True:
    #     client_socket, addr_client = sk1.accept()
    #     print("Dia chi client: {}".format(addr_client))
    #     try:
    #         msg = receive_msg(client_socket)
    #         print("{}:{}".format(client_socket, addr_client))
    #         print("Gui tu client:", msg)
    #         send_msg(client_socket, msg+" tao la server")
    #     except ConnectionError:
    #         print("Error")
    #     finally:
    #         print("Dong ket noi")
    #         client_socket.close()
    while True:
        client_socket, addr_client = sk1.accept()
        print("Gui den client: {}\n".format(addr_client))
        thread = threading.Thread(target=process_client, args=[
                                  client_socket, addr_client], daemon=True)
        thread.start()
