from math import floor
t = int(input())
for x in range(t):
    c = int(input())
    delta = 1-(4*3*(-2*c))
    n = (-1+(delta**(1/2)))/6
    i = floor(n)
    print(i)
# FAZER COM LAMBDA
