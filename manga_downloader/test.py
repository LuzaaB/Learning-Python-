MANGA = {
    "result": "ok",
    "response": "collection",
    "data": [
        {
            "id": "624032a9-c4e7-4ab1-a4d5-3a00627ef860",
            "attributes": {
                "volume": "1",
                "chapter": "6",
                "title": "A Secret Act of Consideration",
                "translatedLanguage": "en",
            }
        },
        {
            "id": "03819860-1da4-4878-b5f6-181b59b416de",
            "attributes": {
                "volume": "1",
                "chapter": "4",
                "title": "The Angel\u2019s Way of Choosing a Gift",
                "translatedLanguage": "en",
            }
        },
        {
            "id": "d32b308b-429b-49a8-9803-1a6093537ec0",
            "attributes": {
                "volume": "1",
                "chapter": "5",
                "title": "The Angel and Picky Eaters",
                "translatedLanguage": "en",
            }
        },
        {
            "id": "e4042607-8af1-46ae-93fd-6bca54cdf50f",
            "attributes": {
                "volume": "1",
                "chapter": "1",
                "title": "Out of Season",
                "translatedLanguage": "en",
            }
        },
        {
            "id": "df83b24b-36dd-4030-aee6-117d3bbb6d23",
            "attributes": {
                "volume": "1",
                "chapter": "2",
                "title": "The Night After the Storm",
                "translatedLanguage": "en",
            }
        },
        {
            "id": "70319332-6357-4dad-829e-91821a655cab",
            "attributes": {
                "volume": "1",
                "chapter": "3",
                "title": "Unsweetened Coffee with a Pinch of Sugar",
                "translatedLanguage": "en",
            }
        },
        {
            "id": "d5017c6d-69bc-46ab-ab3a-5a8bd2de7a0e",
            "attributes": {
                "volume": "1",
                "chapter": "7",
                "title": "A Teddy Bear and Gratitude",
                "translatedLanguage": "en",
            }
        }
    ]
}





length = len(MANGA["data"])
for i in range(length) :
    for j in range(0, length-i-1) :
        
        jth_chap = MANGA["data"][j]  ### chapter_data
        j_val = int(jth_chap["attributes"]["chapter"])
        j_plus_chap = MANGA["data"][j+1]
        j_plus_val = int(j_plus_chap["attributes"]["chapter"])
        
        
        if j_val > j_plus_val:
            temp_store = MANGA["data"][j]
            MANGA["data"][j] = MANGA["data"][j+1]
            MANGA["data"][j+1] = temp_store
            
            # MANGA["data"][j] , MANGA["data"][j+1] = MANGA["data"][j+1] , MANGA["data"][j]
            
        # d="data"
        # c="chapter"
        # a="attributes"
        # if int(MANGA[d][j]["attributes"]["chapter"])>int(MANGA[d][j+1]["attributes"]["chapter"]) :
        #     MANGA[d][j]["attributes"]["chapter"] , MANGA[d][j+1]["attributes"]["chapter"] = MANGA[d][j+1]["attributes"]["chapter"],MANGA[d][j]["attributes"]["chapter"]
        #     MANGA[d][j]["id"],MANGA[d][j+1]["id"] = MANGA[d][j+1]["id"],MANGA[d][j]["id"]
            
            
            
print(MANGA)