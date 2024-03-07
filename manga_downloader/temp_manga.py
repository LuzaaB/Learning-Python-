import requests
import json
import dataclasses
import img2pdf

from typing import List, Dict
from pathlib import Path
from tqdm import tqdm

## sys.argv  
import io
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
            if char in ":/\'\" ":
                newStr += "_"
            else:
                newStr += char
        
        return newStr     


    def download_image_content(self):
        
        img_array = []
        
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
        for page in tqdm(self.page_paths):
            dl_url = PAGE_DL_URL.format(HOST_URL=self.dl_host_url, CHAP_HASH=self.dl_hash, PAGE=page)
            dl_resp = requests.get(dl_url)
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
                
                # swapping
                if first_data.chap_no > second_data.chap_no:
                    temp = first_data
                    self.chapter_list[j] = self.chapter_list[j+1]
                    self.chapter_list[j+1] = temp

    
    def _sort_volume(self):
        for each in self.chapter_list:
            if each.vol_no in self.volume_dict:
                self.volume_dict[each.vol_no].append(each)
            else:
                self.volume_dict[each.vol_no] = []
                self.volume_dict[each.vol_no].append(each)
     
        
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
        
        CHAPTER_LIST = []
        counter = True
        limit = 100
        offset = 0
        chap_list_url = f"{SEARCH_MANGA_URL}/{self.id}/feed"
        while counter:
            chpt_list = requests.get(chap_list_url, params={"translatedLanguage[]":languages, "offset":offset})
            resp  = chpt_list.json()
            CHAPTER_LIST.append(resp["data"])
            if resp["total"] > limit:
                offset += 100
                limit += 100
            elif resp["total"] < limit:
                counter = False
            
        global LAST_UNIQUE_CHAP_ID
        
        for chap_list in CHAPTER_LIST:    
            for each in chap_list:
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
        
        
    def download_and_make_vol_pdf(self, start=None, stop=None):
    
        for volume, chapters in self.volume_dict.items():

            if start is None:
                pass
            elif start > volume:
                continue
            
            if stop is None:
                pass
            elif stop < volume:
                break
            
            print("Downloading volume ", volume)
            # continue
            ###### per volume task   ###
            root_dir = Path(f"{self.sanitized_title}")  
            root_dir.mkdir(exist_ok=True)
            
            pdf_path = root_dir/f"Volume_{volume}.pdf"
            # full_path = "E:\Python\Learning-Python\manga_downloader\"+pdf_path
            full_path = Path('E:')/'Python'/'Learning-Python'/'manga_downloader'/pdf_path
            
            print(pdf_path)
            
            if Path(pdf_path).exists():
                print(Path(full_path).exists())
                print(f'Volume {volume} already exists.\n')
                continue
                
            img_content_list = []
            
            for chap in chapters:                
                print(f"\nDownloading chapter {chap}")
                page_images = chap.download_image_content()
                img_content_list.extend(page_images)
                
            with open(pdf_path, "wb") as f:
                f.write(img2pdf.convert(img_content_list))
            


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
    start = input("Enter start volume/ Enter None/ Press Enter : ")
    stop = input("Enter stop volume/ Enter None/ Press Enter : ")
    
    if start == "" or start == "None":
        start = None
    else:
        start = float(start)
        
    if stop == "" or stop == "None":
        stop = None
    else:
        stop = float(stop)
        
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
    manga.download_and_make_vol_pdf(start, stop)

    
if __name__ == "__main__":
    main() 