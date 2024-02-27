class User:
    pass

# Add instance attributes dynamically
jane = User()
jane.name = "Jane"
jane.job = "Data Engineer"
print(f"{jane.__dict__}")

# Add emthods dynamically
def __init__(self, name, job):
    self.name = name
    self.job = job
    
User.__init__ = __init__
print(f"{User.__dict__}")

linda = User("Linda", "Team Lead")
print(f"{linda.__dict__}")