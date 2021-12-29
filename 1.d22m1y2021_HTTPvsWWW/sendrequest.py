import urllib.request
import urllib.error
# response = urllib.request.urlopen('http://google.com')
# print(response.read())
# print(response.getheader('Content-Type'))  #in ra kiểu dữ liệu server gửi
# print(response.getheader('User-agent'))  #in ra user dùng trình duyệt gì

# res = urllib.request.urlopen("http://python.org")
# print(res.info())
# print(res.getheaders())
# print(res.geturl())  #in ra đg dẫn url
# print(res.status)   #in ra mã xác nhận thành công

# try:
#     res =urllib.request.urlopen("https://www.xvideos.com")
# except urllib.error.HTTPError as e:
#     print("status:",e.code)
#     print("ly do loi:",e.reason)
#     print("url:",e.url)

""" xem trang web này đến trang web(liên kết) này có bn ảnh """

# from urllib.request import urlopen
# import re
# res = urlopen("http://python.org")
# html = res.read()
# urls= re.findall("http[s]{0,1}:\/\/[w]{0,3}[.]{0,1}[a-zA-Z0-9]+(?:\.[a-z]+)+" ,str(html))
# imgs = re.findall(".png|.svg|.jpg|.jpeg|.gif|.ico",str(html))
# print("Link:\n",urls)
# print("so anh:\n",len(imgs))

""" nén và giải mã  """
import urllib.request
import gzip
# req = urllib.request.Request("http://www.vnexpress.net")
# req.add_header('Accept-Language','en') #thêm header trước khi gửi đi
# req.add_header('Accept-Encoding','gzip')
# response = urllib.request.urlopen(req)
# a=response.read()
# print(a,"\n\n\n")
# print("giai nen:")
# content = gzip.decompress(a)
# print(content.splitlines(5))

""" yêu cầu thì là get_header còn phản hồi thì là getheader """
# print(req.get_header('User-agent'))
# print(response.getheader('User-agent'))

""" #cookie """
# import urllib.request as ur
# import http.cookiejar
# import datetime
# cookie_jar = http.cookiejar.CookieJar()
# opener = ur.build_opener(ur.HTTPCookieProcessor(cookie_jar))
# # sử dụng opener để tạo HTTP request và in ra slg cookie của trang đó
# opener.open('https://www.github.com')
# print("số lượng cookie:"+str(len(cookie_jar)))
# # Tạo danh sách để lấy từng cookie
# cookies = list(cookie_jar)
# # in ra các thành phần của 1 cookie
# for i in cookies:
#     print("name: " + i.name)
#     print("value: "+i.value)
#     print("domain: "+i.domain)
#     print(i.expires)
#     try:
#         # đổi từ timestamp sang datetime
#         print(datetime.datetime.fromtimestamp(i.expires))
#     except:
#         pass
#     print('-------')

# """ #hiện url "
# req = ur.Request("http://www.gmail.com")
# r = urllib.parse.urlparse(
#     'http://www.python.org/3/search.html?q=urlparse&area=default%20')
# response = ur.urlopen(req)
# print(response.url)
# print(r)
