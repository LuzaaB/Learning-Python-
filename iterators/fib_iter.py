class FibonacciIterator:
    def __init__(self, stop) -> None:
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (self._next, self._current + self._next)
            return fib_number
        raise StopIteration
    

for num in FibonacciIterator(5):
    print(num)