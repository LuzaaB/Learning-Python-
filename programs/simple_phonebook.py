

li = [
    {
        "name": "Sanskar",
        "phone": 123,
    },
    {
        "name": "Luzaa",
        "phone": 556
    }
]

li *= 10000000
li.append({"name": "Anil", "phone": 123})

def find_number_by_name(name):
    for each in li:
        if each["name"] == name:
            return each["phone"]




print( find_number_by_name("Anil") )