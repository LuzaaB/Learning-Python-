import json
import requests

r = requests.get("https://creativenovels.com/80/volume-9-chapter-38-trigger/")
resp = r.html()
print(resp)