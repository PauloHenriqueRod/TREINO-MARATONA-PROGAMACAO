from math import ceil
n, l, d = [int(n) for n in input().split()]
d /= 1000
litros_bebidos = n*d
print(ceil(litros_bebidos/l)*l)
