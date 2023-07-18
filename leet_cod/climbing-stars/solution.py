def climbStairs(n: int, cache = {}) -> int:
    if n in cache:
        return cache[n]
    if n == 1:
        result = 1

    elif n == 2:
        result =  2
    
    else:
        result = climbStairs(n-1) + climbStairs(n-2)
    cache[n] = result
    return result

while True:
    n = int(input())
    print(climbStairs(n))