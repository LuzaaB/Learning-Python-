
n_term = int(input("Enter the nth term of the fibonacci series :"))

def fibonacci_generator(stop=n_term):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_num = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_num
        
print(list(fibonacci_generator()))
print(list(fibonacci_generator(20)))