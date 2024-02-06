import requests
import json

URL = "https://api.mangadex.org"
SEARCH_URL = f"{URL}/manga"     
CHAPTER_LIST_URL = f"{SEARCH_URL}/"


def write_json(text_data):
    with open("manga_json.json", "w") as f:
        f.write(text_data)


def main():
    inp = input("Name of manga: ")
    
    response = requests.get(SEARCH_URL, params={"title": inp})
    resp = response.json()
    
    write_json(json.dumps(resp, indent=4))
    
    ##### Task: show the title of the first result, if any
    ###  If no result, print an error message and quit
     
    print(json.dumps(resp, indent=4))
    
    
    
    #### Task: Show the first 10 chapters of the first result (array/list slicing)
    #### and also show the titles of the chapters (in english)
    
    
    
    ##### Task: Download a single page of the first chapter and print the response
    
    

if __name__ == "__main__":
    main()
    
    
    
# 