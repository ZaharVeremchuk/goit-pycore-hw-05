from typing import Callable # use function Callable

def caching_fibonacci() -> Callable[[int], int] :
    cache = {} # Create dictonary

    def fibonacci(n):
        if n <= 0: # Condition for 0
            return 0
        elif n == 1: # Condition for 1
            return 1
        elif n in cache.keys(): # If value for digit already in dictionary
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Recursion
            return cache[n]
    return fibonacci;  

fib = caching_fibonacci()

print(fib(10)) # Call inner function
print(fib(15)) # Call inner function