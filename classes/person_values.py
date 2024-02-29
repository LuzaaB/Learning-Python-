from person import Person
from person import Person1

jane = Person("Jane")
print(jane.name)

jane.name = "Jane Doe"
print(jane.name)

john = Person1("John")
print(john.get_name())

john.set_name("John Doe")
print(john.get_name)