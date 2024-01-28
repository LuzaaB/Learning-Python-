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