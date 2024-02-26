import requests
import json
import io
import dataclasses

import img2pdf
from typing import List, Dict
from PIL import Image
from pathlib import Path
from tqdm import tqdm

## sys.argv  
import sys          ## LATER, but before argparse
import argparse     ### argument parsing. FOR LATER>
## os.path or pathlib  

LAST_UNIQUE_CHAP_ID = 9999.0

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
    chap_no: float | None
    vol_no: float | None
    num_pages: int
    
    ### download data    
    dl_hash: str = ""
    dl_host_url: str = ""
    page_paths: List[str] =  dataclasses.field(default_factory=lambda: [])
    

    def __repr__(self):
        return f"<Chapter:{self.chap_no} {self.title}>"
    
    
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
        
        return newStr     


    def download_image_content(self, parent_manga):
        
        img_array = []
        
        ### manage and check the appropriate paths (create if not created)
        folder_path = Path(parent_manga.sanitized_title) / Path(self.sanitized_title) 
        folder_path.mkdir(exist_ok=True, parents=True)
        
        ### fill dl data
        # chap_id_url = f"https://api.mangadex.org/at-home/server/{self.id}"
        chap_id_url = CHAP_ID_URL.format(chapter_id=self.id)
        resp = requests.get(chap_id_url)
        # print(resp.text, resp.status_code)
        parsed_resp = resp.json()
        self.dl_hash = parsed_resp["chapter"]["hash"]
        self.dl_host_url = parsed_resp["baseUrl"]      
        
        for img in parsed_resp["chapter"]["data"]:
            self.page_paths.append(img)
        
        ### actual download
        for idx, page in tqdm(enumerate(self.page_paths)):
            
            if idx == 5:
                break
            
        # for page in self.page_paths:
            dl_url = PAGE_DL_URL.format(HOST_URL=self.dl_host_url, CHAP_HASH=self.dl_hash, PAGE=page)
            dl_resp = requests.get(dl_url)
            # extension = page[page.rindex('.')+1:] 
        # +1 is used to retrieve the character immediately after the last occurance of the given character
            ##    print(extension)
            # actual_filename = f"{idx+1}.{extension}"
            # img_path = folder_path / actual_filename
            # with img_path.open(mode="wb") as f:
            #     f.write(dl_resp.content)
            img_array.append(dl_resp.content)           
            
        return img_array



@dataclasses.dataclass
class Manga:
    id: str
    title: str
    chapter_list: List[Chapter] = dataclasses.field(default_factory=lambda: [])
    volume_dict : Dict[float|None, List[Chapter]] = dataclasses.field(default_factory=lambda: {})
    
    
    @property
    def sanitized_title(self):    
        newStr = ""
        for char in self.title:
            if char in ":/\'\"":
                newStr += "_"
            else:
                newStr += char
        
        return    newStr     
        ##    return self.title.replace(" ", "_").replace(":", )
        
        
    def __repr__(self):
        return f"<Manga {self.title}>"


    def dump_to_file(self):
        with open(f"{self.sanitized_title}.json", "w") as f:
            json.dump(self, f, cls=EnhancedJSONEncoder, indent=4)   
        
        
    def _sort_chapters(self):
        list_len = len(self.chapter_list)
        for i in range(1, list_len):
            for j in range(0, list_len-i):
                first_data = self.chapter_list[j]
                second_data = self.chapter_list[j+1]
                
                ### each time you print, make it so that the j-th and j+1-st chapters 
                ### have some kind of marks that identify them
                ##   print(f'i = {i} \n comparing {first_data} and {second_data}')
                ##   print(f"STATE: i = {i} j = {j} \n", " | ".join([str(c) for c in self.chapter_list]))
                
                # swapping
                if first_data.chap_no > second_data.chap_no:
                    temp = first_data
                    self.chapter_list[j] = self.chapter_list[j+1]
                    self.chapter_list[j+1] = temp
        ##   print(self.chapter_list)

    
    def _sort_volume(self):
        for each in self.chapter_list:
            if each.vol_no in self.volume_dict:
                self.volume_dict[each.vol_no].append(each)
            else:
                self.volume_dict[each.vol_no] = []
                self.volume_dict[each.vol_no].append(each)
        # print("HELLO : ",self.volume_dict)
        
    def get_pretty_vol_dump_str(self):
        """
        Expected output format:
        Vol 1:
            Chapter 1: Dancing in the rain
            Chapter 2
        Vol 2:
            Chapter 3
        """
        # early exit
        if len(self.volume_dict.keys()) == 0:
            return "<Empty>"
        
        return_stri = ""  
        for key,value in self.volume_dict.items():    
            return_stri += "Volume " + str(key) + " : \n"
            list_len = len(value)
            for j in range(list_len) : 
                val = str(value[j])
                return_stri += "\t" + val + "\n"  
        
        return return_stri
                
    
    #  chapList.json ko data use garera
    def download_chapter_data(self):
        """ Downloads and saves the initial chapter data for all available
        chapters from the feed (this does not include the chapter's hash and 
        page filenames or page lists) """        
        
        chap_list_url = f"{SEARCH_MANGA_URL}/{self.id}/feed"
        chpt_list = requests.get(chap_list_url, params={"translatedLanguage[]":languages})
        CHAPTER_LIST = chpt_list.json()

        global LAST_UNIQUE_CHAP_ID
        
        for each in CHAPTER_LIST["data"]:
            chap_id = each["id"]
            chap_title = each["attributes"]["title"]
            
            chap_num = each["attributes"]["chapter"]
            if chap_num is None or chap_num == "":
                chap_num = LAST_UNIQUE_CHAP_ID
                LAST_UNIQUE_CHAP_ID += 1.0
            else:
                chap_num = float(each["attributes"]["chapter"])
            
            vol = each["attributes"]["volume"]
            if vol is None or  vol == "" :
                vol_num = 9999.0
            else:
                vol_num = float(each["attributes"]["volume"])
            
            num_pages = int(each["attributes"]["pages"])
            
            chapter = Chapter(chap_id, chap_title, chap_num, vol_num, num_pages)
            self.chapter_list.append(chapter)
        ##     print(f'chapter list {self.chapter_list}')
        self._sort_chapters()
        
        
    def download_and_make_vol_pdf(self):
    
        for volume, chapters in self.volume_dict.items():
            ###### per volume task   ###
            img_content_list = []
            
            for chap in chapters:
                print(f"\nDownloading chapter {chap}")
                page_images = chap.download_image_content(self)
                img_content_list.extend(page_images)
            
            ## os.path.join(A, B) => A/B
            ### Path(A) / B
            root_dir = Path(f"{self.sanitized_title}")  
            root_dir.mkdir(exist_ok=True)
            
            pdf_path = root_dir / f"Volume {volume}.pdf"
            
            with open(pdf_path, "wb") as f:
                f.write(img2pdf.convert(img_content_list))
            # img_content_list[0].save(pdf_path, "PDF" , 
            #                         resolution=100.0, 
            #                         save_all=True, 
            #                         append_images=img_content_list[1:])
            

def get_first_result(chap_search_url_response):
    results =  chap_search_url_response.json()["data"]
    if len(results) == 0:
        print("NOT FOUND!")
        return None
    
    first = results[0]
    first_id, first_title = first["id"], first["attributes"]["title"]["en"]
    
    return Manga(first_id, first_title)



def main():
    title = input("Enter manga name : ")
    
    # order = {"rating" : "desc" , "followedCount" : "desc"}
    # final_order = {}
    # for key, value in order.items():
    #     final_order[f"order[{key}]"] = value
        
    r = requests.get(SEARCH_MANGA_URL , params = {"title" : title})
    ##, **final_order
    
    manga: Manga = get_first_result(r)
    manga.download_chapter_data()
    manga._sort_volume()
    print(manga.get_pretty_vol_dump_str())
    
    # manga.volume_dict[1.0] = (manga.volume_dict[1.0])[:1]
    manga.download_and_make_vol_pdf()
    # for each in manga.chapter_list[:1]: #
    #     each.download_image_content(manga)
    
    # manga.dump_to_file()
    
if __name__ == "__main__":
    main() 
    

# 1. Directory structure
# 2. from resp.content
#    grouping into volumes