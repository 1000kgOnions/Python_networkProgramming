# import socket
# if __name__=='__main__':
#         sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sk.bind(('127.0.0.1',9050))
#         sk.listen(5)
#         sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         print("Waiting connection for client.....")
#         client, client_addr = sk.accept()

#         print("dia chi client: {}".format(client_addr))
#         while True:
#             filename = 'testfile.txt'
#             f=open(filename, 'rb')
#             l=f.read(1024)
#             client.send(l)
#             while(l):
#                 client.send(l)
#                 l=f.read(1024)
#             f.close()
#         print("DONE")
#         client.close()
#         sk.close()
""" HNAM """
import socket
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',8000))
    sk.listen(5)
    print("Waiting")
    client, addr = sk.accept()
    f=open('testfile.txt','rb')
    l= f.read(8096)
    client.send(l)
    f.close()
    print("Done")
    client.close()
    sk.close()