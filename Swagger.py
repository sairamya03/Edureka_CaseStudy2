# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:05:28 2019

@author: SMACHAV
"""



import requests

link = "https://petstore.swagger.io/v2/swagger.json"
f1 = requests.get(link)
print(f1.text)
