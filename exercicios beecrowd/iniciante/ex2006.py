T = int(input())
A, B, C, D, E = [int(n) for n in input().split()]
certo = 0
lista = list()
lista.append(A)
lista.append(B)
lista.append(C)
lista.append(D)
lista.append(E)
for n in lista:
    if n == T:
        certo += 1
print(certo)
