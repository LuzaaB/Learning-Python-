def square_generator(sequence):
    for item in sequence:
        yield item ** 2
        
for square in square_generator([1,2,3,4,5,6,7,8,9]):
    print(square)