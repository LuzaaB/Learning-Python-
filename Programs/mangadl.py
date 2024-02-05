import requests
import json

URL = "https://api.mangadex.org"
SEARCH_URL = f"{URL}/manga"
CHAPTER_LIST_URL = f"{SEARCH_URL}/"

def main():
    inp = input("Name of manga: ")
    
    response = requests.get(SEARCH_URL, params={"title": inp})
    resp = response.json()
    
    print(json.dumps(resp, indent=4))
    

if __name__ == "__main__":
    main()