lista = []
n1, n2, n3 = [int(n) for n in input().split()]
lista.append(n1)
lista.append(n2)
lista.append(n3)
for c in sorted(lista):
    print(c)
print()
for c in lista:
    print(c)
