# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/ParaphraseQA"
#openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/Word"
accessKey = "41eafa40-2d3b-41a1-9e01-96b9a9d0ce0f"
# question = "YOUR_QUESTION"
# type = "ENGINE_TYPE"
sentence1 = "성탄 전야 미사를 집전하며 프란치스코 교황이 전한 메시지는 '어린이를 향한 관심'입니다."
sentence2 = "프란치스코 교황의 올해 첫 성탄 메시지는 고통받는 어린이를 향한 관심이었습니다."
#word = "인공 두뇌라는 뜻으로"

requestJson = {
"access_key": accessKey,
"argument": {
    "sentence1": sentence1,
    "sentence2": sentence2
    }
}

"""
requestJson = {
    "access_key": accessKey,
    "argument": {
        "word": word
    }
}
"""

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


					

