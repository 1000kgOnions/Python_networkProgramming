import socket
import random
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 6969))
    sk.listen(5)
    client_sk, addr = sk.accept()
    client_sk.send('Menu:\n1,Love\n2,Loto\n3,Quit\nBan hay chon: '.encode('utf-8'))
    data = client_sk.recv(1024).decode()
    while True:
      if data == '1':
        listlove = ['Hello', 'Xin chao', 'Hi', '321']
        index = random.randint(0, len(listlove)-1)
        client_sk.send(f'{listlove[index]}❤🧡💛💚💙💜🤎🖤'.encode('utf-8'))
      elif data == '2':
        index = random.randint(0, 99)
        client_sk.send(f'{index}'.encode('utf-8'))
      elif data == '3':
        client_sk.send('bye'.encode('utf-8'))
        break
      else:
        client_sk.send('Menu:\n1,Love\n2,Loto\n3,Quit\nBan hay chon: '.encode('utf-8'))
      data = client_sk.recv(1024).decode()
    client_sk.close()
    sk.close()
