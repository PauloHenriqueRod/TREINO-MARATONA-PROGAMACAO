def calcular_mdc(numero1, numero2): # Algoritmo de Euclides
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1

def calcular_mmc(numero1, numero2):
    x = calcular_mdc(numero1=numero1, numero2=numero2)
    return numero1*numero2 // x


while True:
    n, a, b = [int(x) for x in input().split()]
    if n == 0:
        break
    c = calcular_mmc(a,b)
    x = n//a
    y = n//b
    z = n//(c)
    print(x+y-z)
