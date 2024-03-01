class SquareIterator:
    
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            square = self._sequence[self._index] ** 2
            self._index += 1
            return square
        
        raise StopIteration
    
for square in SquareIterator([1,2,3,4,5,6,7]):
    print(square)