def fatorial(n, cache={}):
    if n in cache:
        return cache[n]
    
    if n == 0 or n == 1:
        result = 1
    else:
        result = fatorial(n - 1) * n
    
    cache[n] = result
    return result


print(fatorial(5))