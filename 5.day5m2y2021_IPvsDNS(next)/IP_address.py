# ipaddress
# chia mang con,cho địa chỉ ip,chia thành 4 mạng,mạng thuộc lớp naò
# xác định địa chỉ network,địa chỉ host
# từ số mạng con -> số bit của host
import ipaddress
import re

class MyIPv4(ipaddress.IPv4Address):
    @property
    def binary_repr(self, sep=".") -> str:
        """Represent IPv4 as 4 blocks of 8 bits."""
        return sep.join(f"{i:08b}" for i in self.packed)

    @classmethod
    def from_binary_repr(cls, binary_repr: str):
        """Construct IPv4 from binary representation."""
        # Remove anything that's not a 0 or 1
        i = int(re.sub(r"[^01]", "", binary_repr), 2)
        return cls(i)

# A:0-127 B:128-191 C:192-223 D:224-239 E:240-255
LOP_C = '192.168.0.0'  # VD:192.168.0.0/27
if __name__ == '__main__':
    s = int(input("Nhập số bit (0-30):"))
    dc_ip = LOP_C+'/'+str(s)
    print("địa chỉ ip: "+dc_ip)
    # convert thành ip
    ip_net = ipaddress.ip_network(dc_ip)   #định nghĩa mạng

    print("Số địa chỉ: {}".format(ip_net.num_addresses))
    print("dia chi mang: {}".format(ip_net.network_address))
    print("subnet mask: {}".format(ip_net.netmask))
    for i in ip_net.hosts():
        print(i)

    for i in ip_net.subnets():
        print(i)

    dc_dau, dc_cuoi = list(ip_net.hosts())[0], list(ip_net.hosts())[-1]
    print("địa chỉ đầu {0}, địa chỉ cuối {1}".format(dc_dau, dc_cuoi))
    print("địa chỉ broadcast {0}".format(ip_net.broadcast_address))

print(MyIPv4("220.14.9.37").binary_repr)
print(MyIPv4.from_binary_repr("11011100 00001110 00001001 00100101"))
