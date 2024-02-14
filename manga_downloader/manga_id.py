import requests
import json
import os

import dataclasses
from pathlib import Path


## sys.argv  
import sys          ## LATER, but before argparse
import argparse     ### argument parsing. FOR LATER>

## os.path or pathlib  

languages = ["en"]
BASE_URL = "https://api.mangadex.org"
SEARCH_MANGA_URL = f"{BASE_URL}/manga"
CHAPTER_URL = "https://api.mangadex.org/at-home/server/{chap_url_json_response}"
PAGE_DL_URL = "{HOST_URL}/data/{CHAPTER_HASH}/{page}"



### store entire data in dataclasses
### make a printable representation

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
   
   

''' To get the chapter list and sort it in ascending order '''
def get_chap_list(chap_list_response):
    chpt_list = requests.get(chap_list_response, params={"translatedLanguage[]":languages})
    chapter_list = chpt_list.json()
    MANGA = json.dumps(chapter_list, indent = 4)
    with open("chapterList.json","w") as f :
        f.write(MANGA)
    
    # CHAPTER-WISE SORTING
    list_len = len(MANGA["data"])
    for i in range(1, list_len) :
        for j in range(0, list_len-i-1) :
            first_val = int(MANGA["data"][j]["attributes"]["chapter"])
            second_val = int(MANGA["data"][j+1]["attributes"]["chapter"])
            if first_val > second_val :
                temp_val = first_val
                MANGA["data"][j] = MANGA["data"][j+1]
                MANGA["data"][j+1] = temp_val
                # shortcut of the above -->
                # MANGA["data"][j] , MANGA["data"][j+1] = MANGA["data"][j+1] , MANGA["data"][j]                
                
    return MANGA


   
''' To get the chapter id of the ones in english'''
def get_chap_id_list(chap_id_response): 
    chap_id_list = []
    for id in range(len(chap_id_response["data"])) :
        chap_id_list.append(chap_id_response["data"][id]["id"])
    return chap_id_list
    # with open("chapter_id.json","w") as chapterID:
    #     chapterID.write(text)
   
   
 
''' To get the JSON data present in the chapter '''
def get_chap_list_url_json(chap_url_json_response):
    parsed_chap_json_list = []
    for id in range(len(chap_url_json_response)):
        # chapter_url = f"https://api.mangadex.org/at-home/server/{chap_url_json_response}"s
        chapter_url = CHAPTER_URL.format(chap_url_json_response=chap_url_json_response[id])
        # print(f"ID of chapters list page : {chapter_url}")
        chapter_json = requests.get(chapter_url)
        parsed_chap_json = chapter_json.json()
        parsed_chap_json_list.append(parsed_chap_json)
        # text = json.dumps(parsed_chap_json, indent=4)
    return parsed_chap_json_list



''' Download the manga'''
def download(download_response):
    HOST_URL = download_response["baseUrl"]
    CHAPTER_HASH = download_response["chapter"]["hash"]
    data = download_response["chapter"]["data"]
    # # data_saver = CHAPTER_JSON["chapter"]["dataSaver"]

    folder_path = Path("Mangadex")
    folder_path.makedirs()
    
    #os.makedirs(folder_path, exist_ok=True)

    for page in data:
        DOWNLOAD_URL = PAGE_DL_URL.format(HOST_URL=HOST_URL, CHAPTER_HASH=CHAPTER_HASH,page=page)  
        R = requests.get(DOWNLOAD_URL)
        
        page_path = Path(folder_path) / page
        with open(page_path , mode="wb") as f:
            f.write(R.content)
            
    print(f"Downloaded {len(data)} pages.")



def main():
    title = input("Enter manga name : ")
    r = requests.get(SEARCH_MANGA_URL , params = {"title" : title})
    
    CHAPTER_SEARCH_URL = get_chap_search_url(r)
    print(f"Chapter Search url : {CHAPTER_SEARCH_URL}")
    
    CHAPTER_LIST = get_chap_list(CHAPTER_SEARCH_URL)
    
    CHAP_ID_LIST = get_chap_id_list(CHAPTER_LIST)
    print(f"Chapter ID : {CHAP_ID_LIST}")

    CHAPTER_JSON = get_chap_list_url_json(CHAP_ID_LIST)
    
    # DOWNLOAD_ONE_PAGE = download_one_page(CHAPTER_ID)
    
    DOWNLOAD = download(CHAPTER_JSON)
    
    
    
if __name__ == "__main__":
    main()