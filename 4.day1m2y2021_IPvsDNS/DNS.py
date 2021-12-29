import dns.resolver
if __name__ == "__main__":
    # request=dns.resolver.resolve('python.org','A')
    # for i in request:
    #     print("IP:",i.to_text())

    # request=dns.resolver.resolve('mail.google.com','CNAME')
    # for i in request:
    #     print("IP:",i.to_text())

    # request=dns.resolver.resolve('google.com','MX')
    # for i in request:
    #     print("IP:",i.to_text())

    hostname = 'www.vnexpress.net'
    kieu = input("Nhap kieu query (A/CNAME/MX):")
    r = dns.resolver.resolve(hostname, kieu)

    if kieu == 'A':
        print("IP: %s" % [i.to_text() for i in r])
    elif kieu == 'CNAME':
        print("Alias: %s" % [i.to_text() for i in r])
    elif kieu == 'MX':
        # print("Mail server: {}".format(i for i in r))
        print("Mail server: %s" % [i.to_text() for i in r])

