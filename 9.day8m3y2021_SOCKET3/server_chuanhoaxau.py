import socket
"""
#isalnum():true nếu chuỗi có ít nhất 1 ký tự và all ký tự là chữ or số
#capitalize():trả về 1 bản sao của chuỗi với chữ cái đầu viết hoa
#strip('key'):xóa ký tự key ở đầu và cuối chuối,nếu strip() thì mặc định xóa khoảng trắng
"""
def convert_string(st):
    s = st[0].upper() + st[1:]
    # [bỏ bn gtri:lấy bn gtri] tính từ bên trái vd:[1:]~ bỏ 1 gtri ở bên trái
    new = ""
    for i in range(len(s)):
        # if s[i-1] == '.' and s[i+1] != ' ':
        if s[i-1] == '.':
            new = new + ' ' + s[i].upper()
        # elif s[i-1] == ',' and s[i+1] != ' ' and s[i].isupper() == True:
            # new = new + ' ' + s[i].lower()
        elif s[i-1] == ',' and s[i].isupper() == True:
            new = new + s[i].lower()
        elif s[i] == ' ' and not s[i+1].isalnum():
            continue
        else:
            new = new + s[i]
    return new

def c3(s):
    d = [str(i).strip().capitalize().split() for i in s.split('.')]
    c = '. '.join([' '.join(i) for i in d])
    r = ''
    for i in range(len(c)):
        if c[i] == ' ' and not c[i+1].isalnum():
            continue
        r += c[i]
    return r

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9050))
    sk.listen(5)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Waiting connection for client.....")
    client, client_addr = sk.accept()
    print("dia chi client: {}".format(client_addr))
    while True:
        data = client.recv(4096)
        print("server nhận: {}".format(data))
        client.send(convert_string(data.decode('utf-8')).encode('utf=8'))
    client.close()
    sk.close()
#anh ko,Hieu chua.ok