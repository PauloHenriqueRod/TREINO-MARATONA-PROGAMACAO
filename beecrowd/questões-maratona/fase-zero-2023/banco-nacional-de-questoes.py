from math import floor
a,b ,c = [int(n) for n in input().split()]
mat = str(input())
if mat == 'A':
    result = floor(a + (3*b)/2 + (5*c/2))
elif mat == 'B':
    result = floor(b + (2*a)/3 + (5*c)/3)
elif mat == 'C':
    result = floor(c + (2*a)/5 + (3*b)/5)
print(result)