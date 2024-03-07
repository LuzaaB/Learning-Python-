
# dummydata =  [
#     {
#         "value": 4,
#         "volume": 1,
#     },
#     {
#         "value": 3,
#         "volume": 1,  
#     },
#     {
#         "value": 2,
#         "volume": 1,
#     },
#     {
#         "value": 1,
#         "volume": 1,
#     },
#     {
#         "value": 6,
#         "volume": 2,
#     },
#     {
#         "value": 5,
#         "volume": 2,
#     },
#     {
#         "value": 7,
#         "volume": 3,
#     },
#     {
#         "value": 8,
#         "volume": 3,
#     },
#     {
#         "value": 9,
#         "volume": 3,
#     },
#     {
#         "value": 10,
#         "volume": 4,
#     },
#     {
#         "value": 11,
#         "volume": 4,
#     },
#     {
#         "value": 12,
#         "volume": 4,
#     }
# ]

# # after sorting

# # The final data should be of the following form, split by volume
# finaldata = [ [1, 2, 3, 4], [5, 6] ]
# my_final_data = []
# ### also, print all chapters from final_data linearly: 1,2,3,4,5,6
# index = 1
# ### Split into groups on volume boundary
# # Assumption: dummy data already sorted by chapter and volume. Only have to split
# data = []

# for i in range(1, len(dummydata)) :
#     for j in range(0, len(dummydata)-1-i):
#         if dummydata[j]["value"] > dummydata[j+1]["value"] :
#             temp = dummydata[j]
#             dummydata[j] = dummydata[j+1]
#             dummydata[j+1] = temp


# for chapter_data in dummydata:
    
#     if chapter_data["volume"] == index :
#         data.append(chapter_data["value"])
        
#     else :
#         print("BREAK")
#         my_final_data.append(data)
#         index += 1
#         data = []
#         data.append(chapter_data["value"])

# my_final_data.append(data)
# # for values in my_final_data :
# #     print(values,"\n")    

# print(my_final_data)

# list_len = len(my_final_data)
# print(list_len)
# print(range(list_len))

import json
import requests

base_url = "https://api.mangadex.org"
search_manga_url = f"{base_url}/manga"
CHAP_ID_URL = "https://api.mangadex.org/at-home/server/{chapter_id}"


title = input("Enter the name of the manga : ")

r = requests.get(search_manga_url, params={"title" : title})
resp = r.json()["data"]
first = resp[0]
first_id, first_title = first["id"], first["attributes"]["title"]["en"]

total_resp = []
limit = 100
offset = 0
counter = True
while counter:
    chap_list_url = f"{search_manga_url}/{first_id}/feed"
    chap_list = requests.get(chap_list_url, params = {"translatedLanguage[]":"en","offset":offset})
    list_resp = chap_list.json()
    total_resp.append(list_resp["data"])
    if list_resp["total"] > limit:
        offset += 100
        limit += 100
    elif list_resp["total"] < limit:
        # offset = 100 - list_resp["total"]
        counter = False
        

# print(json.dumps(CHAPTER_LIST, indent=4))
with open("K.json", "w") as f:
    f.write(json.dumps(total_resp, indent=4))

# from tqdm import tqdm
# from time import sleep

# pbar = tqdm(total=100)
# for i in range (100):
#     sleep(0.1)
#     pbar.update(1)
    
# pbar = tqdm(["a", "b", "c", "d"]) 
# for char in pbar:
#     sleep(0.25)
#     pbar.set_description("Processing %s" % char)

# from tqdm import tqdm
# from time import sleep
# for i in tqdm(range(0, 100), mininterval = 1,
#                desc ="Text You Want"):
#     sleep(.1)

# from pathlib import Path
# import pathlib
# print(pathlib.Path().absolute())
# from tqdm.notebook import tqdm_notebook
# import time
# for i in tqdm_notebook(range(10)):
#     time.sleep(0.5)