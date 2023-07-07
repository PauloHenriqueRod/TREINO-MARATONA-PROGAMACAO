from math import ceil
voltas, placas_pista = [int(n) for n in input().split()]
total_placas = voltas * placas_pista
for x in range(1, 10):
    if x !=9:
        print(ceil(total_placas*(x/10)), end=' ')
    else:
        print(ceil(total_placas*(x/10)), end='\n')