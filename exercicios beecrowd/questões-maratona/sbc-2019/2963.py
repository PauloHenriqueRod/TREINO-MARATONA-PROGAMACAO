n = int(input())
ganhou = True
for x in range(n):
    carlos = int(input())
    if x == 0:
        maior = carlos
    else:
        if carlos > maior:
            ganhou = False
print('S' if ganhou else 'N')