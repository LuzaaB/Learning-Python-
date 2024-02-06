import requests
import json

MAIN_URL = "https://www.webnovelpub.pro"
SEARCH_URL = f"{MAIN_URL}/novel"


NOVEL_URL = f"{SEARCH_URL}/" + "{input_name}"
CHAPTERS_URL = NOVEL_URL + "/chapters/"

def main(): 
    input_name = input("Enter the slug of Light Novel : ")

    # input : the-beginning-after-the-end-web-novel-11110049
    ## https://www.webnovelpub.pro/novel/the-beginning-after-the-end-web-novel-11110049
    
    url = CHAPTERS_URL.format(input_name=input_name)
    print(url)
    response = requests.get(url)
    
    resp = response.text
    
    with open(f"{input_name}.html", "w") as f:
        f.write(resp)
    

      
    #print(json.dumps(resp, indent=4))
    
if __name__ == "__main__" :
    main()
