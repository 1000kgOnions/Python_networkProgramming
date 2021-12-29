# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:04:49 2021

@author: Admin
"""
# dung vong lap de lay nhieu thong tin cung 1 luc
# import requests
# from bs4 import BeautifulSoup
# if __name__ =='__main__':
#     res = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.YAUNCegzbIU")
#     bs = BeautifulSoup(res.content,'html.parser')
#     sd = bs.find(id ="seven-day-forecast") # sd chua noi dung id
#     sd_items = sd.find_all(class_="tombstone-container")
    # tonight = sd_items[0]
    # print(tonight.prettify())   #prettify() để format lại nội dung thẻ html ta lấy được cho đẹp
    # period = tonight.find(class_="period-name").get_text()
    # short_desc= tonight.find(class_="short-desc").get_text()
    # temp = tonight.find(class_="temp").get_text()
    # # print(period)
    # # print(short_desc)
    # # print(temp)

    # for i in sd_items: #vong lap
    #     period = i.find(class_="period-name").get_text()
    #     short_desc = i.find(class_="short-desc").get_text()
    #     temp = i.find(class_="temp").get_text()
    #     print(period)
    #     print(short_desc)
    #     print(temp+"\n")
