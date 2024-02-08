import requests
import json
import os

import dataclasses
import pathlib    ## proper directory structure, and check if already exists

import sys          ## LATER, but before argparse
import argparse     ### argument parsing. FOR LATER>

## os.path or pathlib  

languages = ["en"]
BASE_URL = "https://api.mangadex.org"
SEARCH_MANGA_URL = BASE_URL + "/manga"



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

    # DOWNLOAD_ONE_PAGE = download_one_page(CHAPTER_ID)
    
    DOWNLOAD = downloading(CHAPTER_JSON)
 
 

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
 
 

# """ For retrieving an IMAGE / DOWNLOADING single image"""
# def download_one_page(image_download_response):
#     img_hash = image_download_response["chapter"]["hash"]
#     img_base_url = image_download_response["baseUrl"]
#     img_quality = "data" # can be "data-saver"
#     img_filename = image_download_response["chapter"][img_quality][0]

#     IMG_URL  = img_base_url+"/" + img_quality+"/" + img_hash+"/" + img_filename
#     resp = requests.get(IMG_URL)

#     with open(img_filename, "wb") as f:
#         f.write(resp.content)



''' Download the manga'''
def downloading(downloading_response):
    HOST_URL = downloading_response["baseUrl"]
    CHAPTER_HASH = downloading_response["chapter"]["hash"]
    data = downloading_response["chapter"]["data"]
    # # data_saver = CHAPTER_JSON["chapter"]["dataSaver"]

    folder_path = "Mangadex/"
    os.makedirs(folder_path, exist_ok=True)

    for page in data:
        DOWNLOAD_URL = HOST_URL + "/data/" +  CHAPTER_HASH +  "/" + page
        
        R = requests.get(DOWNLOAD_URL)
        
        with open(folder_path+"/"+page , mode="wb") as f:
            f.write(R.content)
            
    print(f"Downloaded {len(data)} pages.")



if __name__ == "__main__":
    main()