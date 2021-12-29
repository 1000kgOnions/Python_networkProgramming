# import socket
# if __name__ =='__main__':
#         #tạo socket TCP
#         sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sk.connect(('127.0.0.1',9050))
#         # f = open('file_nhan.txt','wb')
#         with open('file_nhan.txt','wb') as f:
#             while True:
#                 print("receiving")

#                 data = sk.recv(1024)
#                 print("data= {}".format(data))
#                 if not data:
#                     break
#                 f.write(data)
#         sk.close()
#         f.close()
""" HNAM """
import socket
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8000
    addr = (host, port)
    sk.connect(addr)
    f=open("abcnhan.txt","wb")
    l=sk.recv(8096)
    f.write(l)
    f.close()
    print("Done")
    sk.close()