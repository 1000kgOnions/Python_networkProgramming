""" lay dia chi IP """
# import netifaces
# import socket
# if __name__=="__main__":
#     # hostname = socket.gethostname() #lấy tên của máy
#     hostname = "www.python.org"
#     ipadd=socket.gethostbyname(hostname)
#     print("host name: "+hostname)
#     print("Dia chi IP: "+ipadd)
# print(socket.gethostbyname(socket.gethostname())) #lấy IP của máy
# print(socket.gethostbyname('google.com'))   #lấy IP của trang google

""" scan port """
# import socket
# if __name__=="__main__":
    # hostname = socket.gethostname()
    # hostname = input("nhap host: ")  #nhap www. vnexpress.com
    # ipadd=socket.gethostbyname(hostname)
    # print("host name: "+hostname)
    # print("Dia chi IP: "+ipadd)

    # #scan
    # while 1:
    #     port_ = int(input("nhap port: "))
    #     try:
    #         sk = socket.socket()
    #         #connect den IP va port
    #         r = sk.connect(ipadd, port_)   #neu connect dc thi cong dang mo
    #         print("Port " +str(port_)+ " dang mở")
    #         sk.close
    #     except:
    #         print("Port " +str(port_)+ " đã đóng")

""" netifaces """
import netifaces
import socket
if __name__ == "__main__":
    # hostname = socket.gethostname()
    hostname = "python.org"
    ipadd = socket.gethostbyname(hostname)
    print("host name: "+hostname)
    print("Dia chi IP: "+ipadd)

    # lay danh sach netiface (phuong thuc interfaces())
    list_interface = netifaces.interfaces()  #tìm các giao tiếp mạng
    # duyet
    for i in list_interface:
        # ifaddresses(i)
        ip_addrs = netifaces.ifaddresses(i)   #tìm các địa chỉ IP của 1 giao diện mạng i
        if netifaces.AF_INET in ip_addrs:  # AF_INET là ipv4
            # in
            ip_mota = ip_addrs[netifaces.AF_INET]
            ip_mota = ip_mota[0]
            print("Network interface: {}".format(i))
            print("\t IPaddress: {}".format(ip_mota['addr']))
            print("\t Netmask: {}".format(ip_mota['netmask']))
            gateways = netifaces.gateways()
            print("Default gateway: {}".format(gateways['default'][netifaces.AF_INET][0]))
