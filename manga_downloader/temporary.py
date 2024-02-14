import requests
import json
from typing import List

import dataclasses
from pathlib import Path


## sys.argv  
import sys          ## LATER, but before argparse
import argparse     ### argument parsing. FOR LATER>

## os.path or pathlib  

languages = ["en"]
BASE_URL = "https://api.mangadex.org"
SEARCH_MANGA_URL = f"{BASE_URL}/manga"
CHAP_ID_URL = "https://api.mangadex.org/at-home/server/{chapter_id}"
PAGE_DL_URL = "{HOST_URL}/data/{CHAP_HASH}/{PAGE}"



class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
    
        
        
@dataclasses.dataclass
class Chapter:
    
    ## meaningful attribs
    id: str
    title: str 
    chap_no: int
    vol_no: int
    num_pages: int
    
    ### download data    
    dl_hash: str = ""
    dl_host_url: str = ""
    page_paths: List[str] =  dataclasses.field(default_factory=lambda: [])
    
    
    def __repr__(self):
        return f"<Chapter {self.chap_no} {self.title}>"
    
    def __str__(self):
        return self.__repr__()
    
    @property
    def sanitized_title(self):    
        newStr = ""
        for char in self.title:
            if char in ":/\'\"":
                newStr += "_"
            else:
                newStr += char
        
        return    newStr     

    def download_to_disk(self, parent_manga):
        
        ### manage and check the appropriate paths (create if not created)
        
        folder_path = Path(parent_manga.sanitized_title) / Path(self.sanitized_title) 
        folder_path.makedirs(exist_ok=True)
        
        ### fill dl data
        # chap_id_url = f"https://api.mangadex.org/at-home/server/{self.id}"
        chap_id_url = CHAP_ID_URL.format(chapter_id=self.id)
        resp = requests.get(chap_id_url)
        print(resp.text, resp.status_code)
        parsed_resp = resp.json()
        self.dl_hash = parsed_resp["chapter"]["hash"]
        self.dl_host_url = parsed_resp["baseUrl"]      
        
        for img in parsed_resp["chapter"]["data"]:
            self.page_paths.append(img)
        
       ### actual download
        for idx, page in enumerate(self.page_paths):
            dl_url = PAGE_DL_URL(HOST_URL=self.dl_host_url, CHAP_HASH=self.dl_hash, PAGE=page)
        
            extension = page[page.rindex('.')+1:] 
        # +1 is used to retrieve the character immediately after the last occurance of the given character
            print(extension)
            actual_filename = f"{idx+1}.{extension}"
            dl_resp = requests.get(dl_url)
            img_path = folder_path / actual_filename

            with img_path.open(mode="wb") as f:
                f.write(dl_resp.content)



@dataclasses.dataclass
class Manga:
    id: str
    title: str
    chapter_list: List[Chapter] = dataclasses.field(default_factory=lambda: [])
    
    @property
    def sanitized_title(self):    
        newStr = ""
        for char in self.title:
            if char in ":/\'\"":
                newStr += "_"
            else:
                newStr += char
        
        return    newStr     
        #return self.title.replace(" ", "_").replace(":", )
        
    def __repr__(self):
        return f"<Manga {self.title}>"

    def dump_to_file(self):
        with open(f"{self.sanitized_title}.json", "w") as f:
            json.dump(self, f, cls=EnhancedJSONEncoder, indent=4)
            
            
        
    def _sort_chapters(self):
        list_len = len(self.chapter_list)
        for i in range(1, list_len):
            for j in range(0, list_len-i-1):
                first_data = self.chapter_list[j]
                second_data = self.chapter_list[j+1]
                
                ### each time you print, make it so that the j-th and j+1-st chapters 
                ## have some kind of marks that identify them
                
                #print(f"STATE: i = {i} j = {j} ", " | ".join([str(c) for c in self.chapter_list]))
                
                if first_data.chap_no > second_data.chap_no:
                    temp = first_data
                    self.chapter_list[j] = self.chapter_list[j+1]
                    self.chapter_list[j+1] = temp
        
        print(self.chapter_list)
    
    #  chapList.json ko data use garera
    def download_chapter_data(self):
        """ Downloads and saves the initial chapter data for all available
        chapters from the feed (this does not include the chapter's hash and 
        page filenames or page lists) """        
        
        chap_list_url =   f"{SEARCH_MANGA_URL}/{self.id}/feed"
        chpt_list = requests.get(chap_list_url, params={"translatedLanguage[]":languages})
        CHAPTER_LIST = chpt_list.json()
    
       
        for each in CHAPTER_LIST["data"]:
            chap_id = each["id"]
            chap_title = each["attributes"]["title"]
            chap_num = int(each["attributes"]["chapter"])
            vol_num = int(each["attributes"]["volume"])
            num_pages = int(each["attributes"]["pages"])
            
            chapter = Chapter(chap_id, chap_title, chap_num, vol_num, num_pages, )
            self.chapter_list.append(chapter)
        # c = Chapter("asfasfas", "The hero returns", 1, 2, 10)
        # print(c)
        # self.chapter_list.append(c)


        self._sort_chapters()

### store entire data in dataclasses
### make a printable representation

# ''' To access particular contents of the searched manga '''
# def get_first_result(chap_search_url_response):
#     results =  chap_search_url_response.json()["data"]
#     if len(results) == 0:
#         print("NOT FOUND!")
#         return None
    
#     first = results[0]
#     first_id, first_title = first["id"], first["attributes"]["title"]["en"]
    
#     return Manga(first_id, first_title)


   

# ''' To get the chapter list and sort it in ascending order '''
# def get_chap_list(chap_list_response):
#     chpt_list = requests.get(chap_list_response, params={"translatedLanguage[]":languages})
#     chapter_list = chpt_list.json()
#     MANGA = json.dumps(chapter_list, indent = 4)
#     with open("chapList.json","w") as f :
#         f.write(MANGA)
    
#     # CHAPTER-WISE SORTING
#     list_len = len(chapter_list["data"])
#     for i in range(1, list_len) :
#         for j in range(0, list_len-i-1) :
#             main_val = chapter_list["data"]
#             first_data = main_val[j]
#             second_data = main_val[j+1]
#             first_data_val = int(first_data["attributes"]["chapter"])
#             second_data_val = int(second_data["attributes"]["chapter"])
#             if first_data_val > second_data_val :
#                 temp_val = first_data
#                 chapter_list["data"][j] = chapter_list["data"][j+1]
#                 chapter_list["data"][j+1] = temp_val
#                 # shortcut of the above -->
#                 # chapter_list["data"][j] , chapter_list["data"][j+1] = chapter_list["data"][j+1] , chapter_list["data"][j]                
                
#     return chapter_list


   
# ''' To get the chapter id of the ones in english'''
# def get_chap_id_list(chap_id_response): 
#     chap_id_list = []
#     for id in range(len(chap_id_response["data"])) :
#         chap_id_list.append(chap_id_response["data"][id]["id"])
#     return chap_id_list
#     # with open("chapter_id.json","w") as chapterID:
#     #     chapterID.write(text)
   
   
 
# ''' To get the JSON data present in the chapter '''
# def get_chap_list_url_json(chap_url_json_response):
#     parsed_chap_json_list = []
#     for id in range(len(chap_url_json_response)):
#         # chapter_url = f"https://api.mangadex.org/at-home/server/{chap_url_json_response}"s
#         chapter_url = CHAPTER_URL.format(chap_url_json_response=chap_url_json_response[id])
#         # print(f"ID of chapters list page : {chapter_url}")
#         chapter_json = requests.get(chapter_url)
#         parsed_chap_json = chapter_json.json()
#         parsed_chap_json_list.append(parsed_chap_json)
#         # text = json.dumps(parsed_chap_json, indent=4)
#     return parsed_chap_json_list



# ''' Download the manga'''
# def download(download_response):
#     HOST_URL = download_response["baseUrl"]
#     CHAPTER_HASH = download_response["chapter"]["hash"]
#     data = download_response["chapter"]["data"]
#     # # data_saver = CHAPTER_JSON["chapter"]["dataSaver"]

#     folder_path = Path("Mangadex")
#     folder_path.makedirs()
    
#     #os.makedirs(folder_path, exist_ok=True)

#     for page in data:
#         DOWNLOAD_URL = PAGE_DL_URL.format(HOST_URL=HOST_URL, CHAPTER_HASH=CHAPTER_HASH,page=page)  
#         R = requests.get(DOWNLOAD_URL)
        
#         page_path = Path(folder_path) / page
#         with open(page_path , mode="wb") as f:
#             f.write(R.content)
            
#     print(f"Downloaded {len(data)} pages.")



def main():
    title = input("Enter manga name : ")
    r = requests.get(SEARCH_MANGA_URL , params = {"title" : title})
    
    manga = get_first_result(r)
    manga.download_chapter_data()
    #manga.dump_to_file()
    
    # manga.setup_download_directory()
    
    for each in manga.chapter_list[:2]:
        each.download_to_disk(manga)
        
    manga.dump_to_file()
    
    
    # for chapter in first_ten:
    #     print("DOWNLOADING ", chapter)
    #     chapter.download_to_disk()
        
    
    
    
    
    # CHAPTER_SEARCH_URL = manga.get_chapterlist_url()
    # print(f"Chapter Search url : {CHAPTER_SEARCH_URL}")
    
    # # get an overview of all the chapters of that result
    # CHAPTER_LIST = get_chap_list(CHAPTER_SEARCH_URL)
    
    # ### TODO: make an initial structure
    
    
    # ###  get all IDs only
    # CHAP_ID_LIST = get_chap_id_list(CHAPTER_LIST)
    # # print(f"Chapter ID : {CHAP_ID_LIST}")

    # #
    # CHAP_JSON_LIST = get_chap_list_url_json(CHAP_ID_LIST)
    # # print(" JSON list of chapters : ", json.dumps(CHAP_JSON_LIST, indent = 4))
    # with open("JSON_CHAP_LIST.json","w") as f:
    #     f.write(json.dumps(CHAP_JSON_LIST, indent = 4))
        
        
    # DOWNLOAD_ONE_PAGE = download_one_page(CHAPTER_ID)
    
    # DOWNLOAD = download(CHAPTER_JSON)
    
    
    
if __name__ == "__main__":
    main()