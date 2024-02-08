import requests
import json

import dataclasses
import pathlib    ## proper directory structure, and check if already exists

import sys          ## LATER, but before argpare
import argparse     ### argument parsing. FOR LATER>

import os

import  news_article as na

## os.path or pathlib  
languages = ["en"]



"""TO SEARCH FOR THE MANGA"""
BASE_URL = "https://api.mangadex.org"
SEARCH_MANGA_URL = BASE_URL + "/manga"



def get_chap_search_url(response):
    results =  response.json()["data"]
    if len(results) == 0:
        print("NOT FOUND!")
        return None
    
    first = results[0]

    ''' To access particular contents of the searched manga '''
    return SEARCH_MANGA_URL + "/" + first + "/feed"
   
   
   
def main():
    title = input("Enter manga name : ")
    r = requests.get(
        SEARCH_MANGA_URL,
        params={"title": title}
    )
    
    ''' To access chapters '''
    CHAPTER_SEARCH_URL = get_chap_search_url(r)
    print(CHAPTER_SEARCH_URL)
    chpt_list = requests.get(CHAPTER_SEARCH_URL, params={"translatedLanguage[]":languages})
    chapter_list = chpt_list.json()
    # print(json.dumps(chapter_list, indent=4))
    # with open("chapterlist.json","w") as f: # to see the contents in english of chapterlist
    #     f.write(json.dumps(chapter_list, indent=4))

    # for chap in chapter_list["data"] :
    #     chapter = chap["id"]  
    chapter_id = chapter_list["data"][0]["id"]
    print(chapter_id)
    # vol = "60dadee7-0d8b-4ebc-b3a8-887e174f87a5"
    CHAPTER_URL = "https://api.mangadex.org/at-home/server/" + chapter_id
    print(CHAPTER_URL)
    chapter_json = requests.get(CHAPTER_URL)
    chap_json = chapter_json.json()
    text = json.dumps(chap_json, indent=4)
    # with open("chapter_id.json","w") as chapterID:
    #     chapterID.write(text)
        

    """ For retrieving an IMAGE / DOWNLOADING single image"""
    img_hash = chap_json["chapter"]["hash"]
    img_base_url = chap_json["baseUrl"]
    img_quality = "data" # can be "data-saver"
    img_filename = chap_json["chapter"][img_quality][0]

    IMG_URL  = img_base_url+"/" + img_quality+"/" + img_hash+"/" + img_filename
    resp = requests.get(IMG_URL)

    with open(img_filename, "wb") as f:
        f.write(resp.content)


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
    

if __name__ == "__main__":
    main()