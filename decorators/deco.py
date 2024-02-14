def print_res(func):
    
    def wrapped_func(*args, **kwargs):
        print("I am calling the function ", func, " with args ", args, "and kwargs ", kwargs)
        return func(*args, **kwargs)
    
    return wrapped_func



### add d
###  add -> decorator -> enhanced addd
###    call()               call()

def add(a, b):
    return a + b 

@print_res
def another_add(a, b):
    return a + b

add = print_res(add)

print(add(1, 2))
print("another add ", another_add(3, 5))
