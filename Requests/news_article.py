import requests
import json

response = requests.get('https://www.webnovelpub.pro/novel/the-beginning-after-the-end-548/chapter-428-16091321')
# resp = response.json()   # the data will be in JSON format
resp = response.text   #the data will be in text format
# print(json.dumps(resp, indent=4))
print(resp)
# print("Print each key-value pair from JSON response")
# for key,value in resp.items() :
#     print(key," : ",value)