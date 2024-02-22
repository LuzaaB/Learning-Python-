
# dummydata =  [
#     {
#         "value": 4,
#         "volume": 1,
#     },
#     {
#         "value": 3,
#         "volume": 1,  
#     },
#     {
#         "value": 2,
#         "volume": 1,
#     },
#     {
#         "value": 1,
#         "volume": 1,
#     },
#     {
#         "value": 6,
#         "volume": 2,
#     },
#     {
#         "value": 5,
#         "volume": 2,
#     },
#     {
#         "value": 7,
#         "volume": 3,
#     },
#     {
#         "value": 8,
#         "volume": 3,
#     },
#     {
#         "value": 9,
#         "volume": 3,
#     },
#     {
#         "value": 10,
#         "volume": 4,
#     },
#     {
#         "value": 11,
#         "volume": 4,
#     },
#     {
#         "value": 12,
#         "volume": 4,
#     }
# ]

# # after sorting

# # The final data should be of the following form, split by volume
# finaldata = [ [1, 2, 3, 4], [5, 6] ]
# my_final_data = []
# ### also, print all chapters from final_data linearly: 1,2,3,4,5,6
# index = 1
# ### Split into groups on volume boundary
# # Assumption: dummy data already sorted by chapter and volume. Only have to split
# data = []

# for i in range(1, len(dummydata)) :
#     for j in range(0, len(dummydata)-1-i):
#         if dummydata[j]["value"] > dummydata[j+1]["value"] :
#             temp = dummydata[j]
#             dummydata[j] = dummydata[j+1]
#             dummydata[j+1] = temp


# for chapter_data in dummydata:
    
#     if chapter_data["volume"] == index :
#         data.append(chapter_data["value"])
        
#     else :
#         print("BREAK")
#         my_final_data.append(data)
#         index += 1
#         data = []
#         data.append(chapter_data["value"])

# my_final_data.append(data)
# # for values in my_final_data :
# #     print(values,"\n")    

# print(my_final_data)

# list_len = len(my_final_data)
# print(list_len)
# print(range(list_len))

data = { 
        1: ["chap1", "chap2", "chap3"],
        2: ["chap4", "chap5", "chap6"],
        3: ["chap7", "chap8", "chap9"],
        4: ["chap10", "chap11", "chap12"],
        5: ["chap13", "chap14", "chap15"],
        6: ["chap16", "chap17", "chap18"],
        7: ["chap19", "chap20", "chap21"],
        }

final_data = ""
for key, value in data.items():
    print("KEY :", key)
    print("VALUE : ", value)

    final_data += "Volume " + str(key) + " : " + "\n"
    len = len(value)
    for i in range(len):
        final_data += value[i] + "\n"

print(f"FINAL VALUE AFTER ARRANGING : {final_data}")