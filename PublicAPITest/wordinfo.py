# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/Word"
accessKey = "41eafa40-2d3b-41a1-9e01-96b9a9d0ce0f"

word = "탱크"

requestJson = {
    "access_key": accessKey,
    "argument": {
        "word": word
    }
}

http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))


					

