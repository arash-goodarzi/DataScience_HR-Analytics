"""
Created on Sun Feb  8 01:03:50 2022

@author: arash

test app via python
"""

import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, headers=headers, json=data)

r.json()
print(r.json())