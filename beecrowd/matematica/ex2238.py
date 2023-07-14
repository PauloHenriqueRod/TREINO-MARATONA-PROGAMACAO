from math import ceil, sqrt

def solve(a: int, b:int, c:int, d:int)->int:
    for i in range(a, ceil(sqrt(c)), a):
        if i%b!=0 and d%i!=0:
            return i
    i = int(c/2)
    if i % a == 0 and i % b != 0 and d % i != 0 and c % i == 0:
        return i
    i = int(c)
    if i % a == 0 and i % b != 0 and d % i != 0 and c % i == 0:
        return i
    return -1


x,y,z,w = [int(n) for n in input().split()]
print(solve(x,y,z,w))