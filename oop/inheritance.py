# Inheritance
class SchoolMember():
    """Represents any school member"""                                           
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        print(f"(Initialized SchoolMember {self.name})")
        
    def tell(self) :
        """Tell my details"""
        print(f'Name:"{self.name}" Age:"{self.age}"', end=" ")
        
class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self, name, age, salary):
        # super().__init__(name, age)
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        
    def tell(self):
        SchoolMember.tell(self)
        print(f'Salary:"{self.salary}"')
        
class Student(SchoolMember):
    """Represents a student"""
    def __init__(self, name, age, marks):
        # super().__init__(name, age)
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        
    def tell(self):
        SchoolMember.tell(self)
        print(f'Marks:"{self.marks}"')
        
t = Teacher('Mr. Rai', 40, 30000)
s = Student('John', 12, 80)

# prints a blank line
print()

t.tell()
s.tell()