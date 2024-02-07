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
chapter = chapter_list["data"][0]["id"]
print(chapter)
# vol = "60dadee7-0d8b-4ebc-b3a8-887e174f87a5"
CHAPTER_URL = "https://api.mangadex.org/at-home/server/" + chapter
print(CHAPTER_URL)



"""FOR DOWNLOADING"""
# # r = requests.get(f"{base_url}/at-home/server/{chapter_id}")
# CHAPTERS = requests.get(CHAPTER_URL)
# r_json = CHAPTERS.json()

# host = r_json["baseUrl"]
# chapter_hash = r_json["chapter"]["hash"]
# data = r_json["chapter"]["data"]
# # data_saver = r_json["chapter"]["dataSaver"]


# folder_path = "Mangadex/"+"60dadee7-0d8b-4ebc-b3a8-887e174f87a5"
# os.makedirs(folder_path, exist_ok=True)



# for page in data:
#     DOWNLOAD_URL = host + "/data/" +  chapter_hash +  "/" + page
    
#     R = requests.get(DOWNLOAD_URL)
    
#     with open(folder_path+"/"+page , mode="wb") as f:
#         f.write(R.content)
        
# print(f"Downloaded {len(data)} pages.")