n = int(input())
numeros = [int(n) for n in input().split()]
numeros_indexados = [(numeros[i], i) for i in range(n)]
numeros_indexados.sort(key = lambda x:x[0])
voltas = 1
for x in range(n-1):
    if numeros_indexados[x][1] > numeros_indexados[x+1][1]:
        voltas += 1
print(voltas)