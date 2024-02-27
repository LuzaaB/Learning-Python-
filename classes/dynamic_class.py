class Record:
    """Hold a record of data"""
    
john = {
    "name" : "John",
    "position" : "Python Developer",
    "department" : "Engineering",
    "salary" : 800000,
    "hire_date" : "2020-01-01",
    "is_manager" : False
}

john_record = Record()

for field, value in john.items():
    setattr(john_record, field, value)
    
print(f"{john_record.name}")
print(f"{john_record.department}")
print(f"{john_record.__dict__}")