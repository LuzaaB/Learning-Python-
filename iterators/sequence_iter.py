class SequenceIterator:
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self.__seq = sequence  # truly hidden
        self._index = 0
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        
        self._index = 0
        raise StopIteration
        
# syntactic sugar

seq = SequenceIterator("Luzaa Byanjankar")

###
iterator = iter(seq)
itertor = seq.__iter__()

item = next(iterator)
while True:
    print(item)
    try:
        item = next(iterator)
    except StopIteration:
        break
    
for each in seq:
    print(each)
    
print("2nd loop")

for each in seq:
    print(each)