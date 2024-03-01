from datetime import datetime

class Employee:
    company = "Sarbbham"
    
    def __init__(self, name, birth_date) -> None:
        self.name = name
        self.birth_date = birth_date
        
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = datetime.fromisoformat(value)
        
    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(
            today.year,
            self.birth_date.month,
            self.birth_date.day
        )
        if today < birthday:
            age -= 1
        return age
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
    
    def __str__(self) -> str:
        return f"{self.name} is {self.compute_age()} years old"
    
    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}()"
            f"name = {self.name}, "
            f"birth_date = '{self.birth_date.strftime('%Y-%m-%d')}')"
        )
        
        
# Values
john = Employee("John Doe", "1998-12-04")
print(john.company)
print(john.name)
print(john.compute_age)
print(john)

jane_data = {"name" : "Jane Doe", "birth_date" : "2001-05-15"}
jane = Employee.from_dict(jane_data)
print(jane)