import requests
import httplib
import json
data = {"username":"afadfa","password":"123456","email":"adfa2@cenling.com"}
headers = {"Content-Type":"application/json","Accept":"text/plain"}
conn = httplib.HTTPConnection('127.0.0.1:8000')
conn.request("POST","/rest/register/user/",json.dumps(data),headers)
