def tribonacci(n:int, cache = {}):
    lista = [0, 1, 1]
    if n <= 2:
        return lista[n]
    for i in range(3, n+1):
        lista.append(lista[i-3]+lista[i-2]+lista[i-1])
    return lista[n]



while True:
    n = int(input())
    print(tribonacci(n))