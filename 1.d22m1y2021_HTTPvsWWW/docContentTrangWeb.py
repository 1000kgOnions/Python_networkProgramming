from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    #doc content trang web
    # url = 'http://brainjar.com/java/host/test.html'
    url = "http://www.vnexpress.net"
    # page = urlopen(url)
    headers = requests.utils.default_headers()
    page = requests.get(url,headers)
    contents = BeautifulSoup(page.content,'html.parser')
    # print(content)
    # print(contents.prettify())
    print(contents.title.name)
    contents
    print(contents.title.string)
    print(contents.find_all("a"))