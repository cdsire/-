# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


url = "http://10.36.131.71:8888/login/"

r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
csrf_input = soup.find(name="input",type="hidden")
csrf_name = csrf_input.attrs.get("name")
csrf_value = csrf_input.attrs.get("value")

payload = {}
payload["username"] = "admin"
payload["password"] = "qianfeng"
res = requests.post(url=url,data=payload)
print(res.content.decode())

