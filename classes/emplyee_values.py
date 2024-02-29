from employee import Employee

john = Employee("John Doe", "1998-12-04")
print(john.company)
print(john.name)
print(john.compute_age)
print(john)

jane_data = {"name" : "Jane Doe", "birth_date" : "2001-05-15"}
jane = Employee.from_dict(jane_data)
print(jane)