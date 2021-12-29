# # lấy tình hình thời tiết của thành phố bất kỳ
import requests
def laydulieu(query):
    req = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query+'&APPID=ea09b842ea465ca396dbddb1ca965382&units')
    return req.json()


if __name__ == '__main__':
    city = input("Nhap thanh pho: ")
    query = 'q='+city
    d = laydulieu(query)
    print(d)
    print("{}'s temperature:{} degree".format(city, d['main']['temp']))
    print("Do am: {}".format(d['main']['humidity']))
    print("Toc do gio: {}m/s".format(d['wind']['speed']))
    print("Mo ta:{}".format(d['weather'][0]['description']))
    print("Thoi tiet: {}".format(d['weather'][0]['main']))
