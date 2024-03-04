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

class RangeIterator:
    def __init__(self, start=0, stop=None, step=None) -> None:
        if stop is None:
            stop, start = start, 0
        if step is None:
            step = 1
        self._range = range(start, stop, step)
        self._iter = iter(self._range)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            self._iter = iter(self._range)
            raise
        
numbers = RangeIterator(2,10,2)
for num in numbers:
    print(num)
print(list(numbers))