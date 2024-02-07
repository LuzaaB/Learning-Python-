import requests
import json
import os

languages = ["en"]



"""TO SEARCH FOR THE MANGA"""
BASE_URL = "https://api.mangadex.org"
SEARCH_MANGA_URL = BASE_URL + "/manga"
title = input("Enter manga name : ")
r = requests.get(
    SEARCH_MANGA_URL,
    params={"title": title}
)

# print([manga["id"] for manga in r.json()["data"]])



"""MANGA SEARCH"""
for manga in r.json()["data"] :
    first = manga["id"]
print(first)
# first = "f65444dc-3694-4e31-a166-8afb2938ed55"

''' To access particular contents of the searched manga '''
CHAPTER_SEARCH_URL = SEARCH_MANGA_URL + "/" + first + "/feed"
print(CHAPTER_SEARCH_URL)
chpt_list = requests.get(CHAPTER_SEARCH_URL, params={"translatedLanguage[]":languages})
chapter_list = chpt_list.json()
# print(json.dumps(chapter_list, indent=4))



''' To access chapters '''
# for chap in chapter_list["data"] :
#     chapter = chap["id"]
chapter_id = chapter_list["data"][0]["id"]
print(chapter_id)
# vol = "60dadee7-0d8b-4ebc-b3a8-887e174f87a5"
CHAPTER_URL = "https://api.mangadex.org/at-home/server/" + chapter_id
print(CHAPTER_URL)
# chapter_json = requests.get(CHAPTER_URL)
# chap_json = chapter_json.json()
# text = json.dumps(chap_json, indent=4)
# with open("chapter_id.json","w") as chapterID:
#     chapterID.write(text)
    

# """FOR DOWNLOADING"""
# # # r = requests.get(f"{base_url}/at-home/server/{chapter_id}")
# CHAPTERS = requests.get(CHAPTER_URL)
# CHAPTER_json = CHAPTERS.json()

# HOST_URL = CHAPTER_json["baseUrl"]
# CHAPTER_HASH = CHAPTER_json["chapter"]["hash"]
# data = CHAPTER_json["chapter"]["data"]
# # # data_saver = CHAPTER_json["chapter"]["dataSaver"]


# folder_path = "Mangadex/"+chapter_id
# os.makedirs(folder_path, exist_ok=True)



# for page in data:
#     DOWNLOAD_URL = HOST_URL + "/data/" +  CHAPTER_URL +  "/" + page
    
#     R = requests.get(DOWNLOAD_URL)
    
#     with open(folder_path+"/"+page , mode="wb") as f:
#         f.write(R.content)
        
# print(f"Downloaded {len(data)} pages.")