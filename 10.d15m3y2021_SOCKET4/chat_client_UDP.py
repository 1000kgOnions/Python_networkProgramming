import socket
""" client """
if __name__ == '__main__':
        # tạo socket TCP
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
          data=input("Nhap: ")
          sk.sendto(data.encode('utf8'),('127.0.0.1',9050))
          if data == 'bye':
            break
          data, addr= sk.recvfrom(1024)
          print(data.decode('utf8'))
        sk.close()