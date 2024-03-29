def fatorial(n, cache={}):
    if n in cache:
        return cache[n]
    
    if n == 0 or n == 1:
        result = 1
    else:
        result = fatorial(n - 1) * n
    
    cache[n] = result
    return result


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(fatorial(m+n-2)/(fatorial(m-1)*fatorial(n-1)))
        