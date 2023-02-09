num = int(input())
for x in range(num):
    a, b = [int(n) for n in input().split()]
    numero = a**b
    print(len(str(numero)))
