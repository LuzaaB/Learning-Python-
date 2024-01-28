# methods have "self"
class Person :
    def say_hi(self):
        print('Hello, how are you')

Person().say_hi()



# "__init__" method
class person:
    def __init__(self,name):
        self.name = name
        
    def say_hello(self):
        print('Hello, my name is', self.name)
        
person('John').say_hello()



# Class and Object Variable
class Robot :
    """Represents a robot, with a name."""
    # class variable, counting the number of robots
    population = 0
    def __init__(self,name):
        """"Initializes the data."""
        self.name = name
        print(f"(Initializing {self.name})")
        
        # When this robot is created, the population is increases
        Robot.population += 1
    
    def die(self):
        """I am dying."""
        print(f"{self.name} is being destroyed.")
        
        Robot.population -= 1
        
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else :
            print(f"There are still {Robot.population} robots working")
        
    def speak(self):
        """Greeting by the robot"""
        print(f"Greetings my master calls me {self.name}")
        
    @classmethod
    def how_many(cls) :
        """Prints the current population"""
        print(f"We have {cls.population} robots")
        
rob1 = Robot("R2-D2")
rob1.speak()
Robot.how_many()

rob2 = Robot("C-3PO")
rob2.speak()
Robot.how_many()

print("\nRobots can do some work here \n")

print("Robots have completed their work. Destroy them")
rob1.die()
rob2.die()

Robot.how_many() 



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
        self.maarks = marks
        
    def tell(self):
        SchoolMember.tell(self)
        print(f'Marks:"{self.marks}"')
        
t = Teacher('Mr. Rai', 40, 30000)
s = Student('John', 12, 80)

# prints a blank line
print()

t.tell()
s.tell()