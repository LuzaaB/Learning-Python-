from sequence_iter import SequenceIterator

class Iterable:
    def __init__(self, sequence) -> None:
        self.sequence = sequence
        
    def __iter__(self) :
        return SequenceIterator(self.sequence)
    
for value in Iterable([1,2,3,4]):
    print(value)
    
    
    
numbers_error = Iterable([1,2,3,4])
next(numbers_error) # will show error

letters_error = "ABCD"
next(letters_error)

fruits_error = ["apple", "banana", "pineapple", "grapes"]
next(fruits_error)

fruits = ["strawberry", "mango", "litchi", "lemon", "orange"]
iter(fruits)

iter(42)
# to see if an object is iterable or not iter() can be used. if you get an iterator back, then the object is 
# iterable, if you get an error then the object isn't iterable