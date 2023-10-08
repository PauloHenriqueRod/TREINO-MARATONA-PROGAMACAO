def calcular_mdc(numero1, numero2):
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1
n = int(input())
for x in range(n):
    a,b = [int(n) for n in input().split()]
    print(calcular_mdc(a, b))