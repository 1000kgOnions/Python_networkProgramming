# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:37:38 2021

@author: Admin
"""
# lay request theo yeu cau
import requests
query = {'q':'river','order':'popular','min_width':'800','min_height':'600'}
req = requests.get("https://pixabay.com/images/search",params=query)
print(req.headers)