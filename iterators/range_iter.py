# class RangeIterator:
#     def __init__(self, *args) -> None:
#         if stop is None:
#             stop, start = start, 0
#         if step is None:
#             step = 1
#         self._range = range(start, stop, step)
#         self._iter = iter(self._range)
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         try:
#             return next(self._iter)
#         except StopIteration:
#             self._iter = iter(self._range)
#             raise
        
# numbers = RangeIterator(2,10,2)
# for num in numbers:
#     print(num)
# print(list(numbers))



##### ASSIGNMENT ITERAOTR 1:
### implement a class Range, that behaves like python's range

####    Range(N) => 0 to N-1
####    Range(i, j) => i to j-1
####    Range(i, j, step) => {i, i+step, i+2*step}


####   for i in Range(10):
#          print(i)
##
#
####   must be repeatable after finish
###### must NOT have a pre-stored sequence: only lower and upper limits

class Range:
    
    def __init__(self, *args) -> None:
        print(f"args: ", args)
        print(f"First val :", args[0])
        print(f"Second val :", args[1])
        # print(f"Third val :", args[2])
        print(range(10))
        
        self.step = 1
        
        if len(args) == 1:
            self.start = 0
            self.stop = int(args[0])
        elif len(args) == 2:
            self.start = int(args[0])
            self.stop = int(args[1])
        elif len(args) == 3:
            self.start = int(args[0])
            self.stop = int(args[1]) 
            self.step = int(args[2])
        
        self.current = self.start
            
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.stop:
            temp = self.current
            self.current += self.step
            return temp
        
        self.current = self.start
        raise StopIteration()
        
        
        
    
    
    
test = Range(1, 10, 2)
print(list(test))
print(list(test))

