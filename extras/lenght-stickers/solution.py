n = int(input())
lista = [int(n) for n in input().split()]
lista.sort()
if n % 2 == 0:
    x = lista[int(n/2)]
    y = lista[int((n/2)) - 1]
    a = sum([abs(lista[i] - x) for i in range(n)])
    b = sum([abs(lista[i] - y) for i in range(n)])
    print(min(a, b))
else:
    x = lista[int((n-1)/2)]
    print(sum([abs(lista[i] - x) for i in range(n)]))