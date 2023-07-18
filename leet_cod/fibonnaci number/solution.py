def fib(n: int, cache = {}) -> int:
    if n in cache:
        return cache[n]
    
    if n == 0 or n == 1:
        result = n
    
    else:
        result = fib(n-1) + fib(n-2)
    
    cache[n] = result
    return result


while True:
    n = int(input())
    print(fib(n))