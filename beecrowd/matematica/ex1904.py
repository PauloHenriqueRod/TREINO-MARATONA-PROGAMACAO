def paridade(x):
    n = 2
    par = 0
    while n <= x:
        par += x // n
        n*=2
    return par

def count_primos(n, m):
    if not (n > m):
        aux = n
        n = m
        m = aux
    if n <= 1:
        return 0
    total = n+1
    prime = [1]*(n+1)
    prime[0] = prime[1] = 0 # prime[0] = 0 and prime[1] = 1
    total = total - 2

    for i in range(2,int(n**0.5) + 1):
        if prime[i] == 1:
            if i < m:
                total -= 1
            for j in range(i**2, n+1, i):
                if prime[j] == 1:
                    total -= 1
                prime[j] = 0
    return total
    
n, m = [int(x) for x in input().split()]
x = abs(n-m)
if x==0:
    print('?')
else:
    quant_primos = count_primos(n, m)
    if quant_primos == 0:
        print("Bob")
    else:
        resposta = paridade(quant_primos+x-1) - (paridade(x)+paridade(quant_primos-1))
        if resposta>0:
            print('Bob')
        else:
            print('Alice')