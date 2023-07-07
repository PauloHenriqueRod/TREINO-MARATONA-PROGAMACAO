n = int(input())
x = input().split()
menor = 0
for i in range(n):
    if i == 0:
        menor = int(x[i])
        pos = i
    else:
        if int(x[i]) < int(menor):
            menor = x[i]
            pos = i
print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")
