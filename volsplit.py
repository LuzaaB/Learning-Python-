
dummydata =  [
    {
        "value": 4,
        "volume": 1,
    },
    {
        "value": 3,
        "volume": 1,  
    },
    {
        "value": 2,
        "volume": 1,
    },
    {
        "value": 1,
        "volume": 1,
    },
    {
        "value": 6,
        "volume": 2,
    },
    {
        "value": 5,
        "volume": 2,
    },
    {
        "value": 7,
        "volume": 3,
    },
    {
        "value": 8,
        "volume": 3,
    },
    {
        "value": 9,
        "volume": 3,
    },
    {
        "value": 10,
        "volume": 4,
    },
    {
        "value": 11,
        "volume": 4,
    },
    {
        "value": 12,
        "volume": 4,
    }
]

# after sorting

# The final data should be of the following form, split by volume
finaldata = [ [1, 2, 3, 4], [5, 6] ]
my_final_data = []
### also, print all chapters from final_data linearly: 1,2,3,4,5,6
index = 1
### Split into groups on volume boundary
# Assumption: dummy data already sorted by chapter and volume. Only have to split
data = []

for i in range(1, len(dummydata)) :
    for j in range(0, len(dummydata)-1-i):
        if dummydata[j]["value"] > dummydata[j+1]["value"] :
            temp = dummydata[j]
            dummydata[j] = dummydata[j+1]
            dummydata[j+1] = temp


for chapter_data in dummydata:
    
    if chapter_data["volume"] == index :
        data.append(chapter_data["value"])
        
    else :
        print("BREAK")
        my_final_data.append(data)
        index += 1
        data = []
        data.append(chapter_data["value"])

my_final_data.append(data)
# for values in my_final_data :
#     print(values,"\n")    

print(my_final_data)