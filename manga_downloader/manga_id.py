import requests
import json
import os

import dataclasses
import pathlib    ## proper directory structure, and check if already exists

import sys          ## LATER, but before argpare
import argparse     ### argument parsing. FOR LATER>

## os.path or pathlib  

languages = ["en"]

BASE_URL = "https://api.mangadex.org"
SEARCH_MANGA_URL = BASE_URL + "/manga"



''' To access particular contents of the searched manga '''
def get_chap_search_url(chap_search_url_response):
    results =  chap_search_url_response.json()["data"]
    if len(results) == 0:
        print("NOT FOUND!")
        return None
    
    first = results[0]["id"]
    print("ID of the first manga in the list : "+first)
    chap_search_url = f"{SEARCH_MANGA_URL}/{first}/feed"
    return chap_search_url
   
   
   
''' To get the chapter id of the ones in english'''
def get_chap_id(chap_id_response):
    chpt_list = requests.get(chap_id_response, params={"translatedLanguage[]":languages})
    chapter_list = chpt_list.json()
    # print(json.dumps(chapter_list, indent=4))
    # with open("chapterlist.json","w") as f: # to see the contents in english of chapterlist
    #     f.write(json.dumps(chapter_list, indent=4))

    # for chap in chapter_list["data"] :
    #     chapter = chap["id"]  
    chapter_id = chapter_list["data"][0]["id"]
    # print(chapter_id)
    return chapter_id
    # with open("chapter_id.json","w") as chapterID:
    #     chapterID.write(text)
   
   
 
''' To get the JSON data present in the chapter '''
def get_chap_url_json(chap_url_json_response):
    chapter_url = "https://api.mangadex.org/at-home/server/" + chap_url_json_response
    print("ID of chapters list page : "+chapter_url)
    chapter_json = requests.get(chapter_url)
    parsed_chap_json = chapter_json.json()
    text = json.dumps(parsed_chap_json, indent=4)
    return text
 
 
   
def main():
    title = input("Enter manga name : ")
    r = requests.get(
        SEARCH_MANGA_URL,
        params={"title": title}
    )
    
    CHAPTER_SEARCH_URL = get_chap_search_url(r)
    print("Chapter Seacrh url : "+CHAPTER_SEARCH_URL)
    
    CHAPTER_ID = get_chap_id(CHAPTER_SEARCH_URL)
    print("Chapter ID"+CHAPTER_ID)

    CHAPTER_JSON = get_chap_url_json(CHAPTER_ID)

    # """FOR DOWNLOADING"""
    # # # r = requests.get(f"{base_url}/at-home/server/{chapter_id}")
    # # # CHAPTERS = requests.get(CHAPTER_URL)
    # # # CHAPTER_json = CHAPTERS.json()

    # HOST_URL = CHAPTER_JSON["baseUrl"]
    # CHAPTER_HASH = CHAPTER_JSON["chapter"]["hash"]
    # data = CHAPTER_JSON["chapter"]["data"]
    # # # data_saver = CHAPTER_JSON["chapter"]["dataSaver"]

    # folder_path = "Mangadex/"+chapter_id
    # os.makedirs(folder_path, exist_ok=True)

    # for page in data:
    #     DOWNLOAD_URL = HOST_URL + "/data/" +  CHAPTER_URL +  "/" + page
        
    #     R = requests.get(DOWNLOAD_URL)
        
    #     with open(folder_path+"/"+page , mode="wb") as f:
    #         f.write(R.content)
            
    # print(f"Downloaded {len(data)} pages.")
    
    
    
    # """ For retrieving an IMAGE / DOWNLOADING single image"""
    # img_hash = CHAPTER_ID["chapter"]["hash"]
    # img_base_url = CHAPTER_ID["baseUrl"]
    # img_quality = "data" # can be "data-saver"
    # img_filename = CHAPTER_ID["chapter"][img_quality][0]

    # IMG_URL  = img_base_url+"/" + img_quality+"/" + img_hash+"/" + img_filename
    # resp = requests.get(IMG_URL)

    # with open(img_filename, "wb") as f:
    #     f.write(resp.content)

if __name__ == "__main__":
    main()