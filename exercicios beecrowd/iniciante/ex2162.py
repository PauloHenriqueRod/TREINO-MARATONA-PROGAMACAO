n = int(input())
x = input().split()
lista = []
pico_vale = [1, 2]
a = 0
for i in range(n):
    lista += [int(x[i])]
if lista[1] > lista[0]:
    pico_vale[0] = 'vale'
    pico_vale[1] = 'pico'
else:
    pico_vale[0] = 'pico'
    pico_vale[1] = 'vale'
for x in range(2, n):
    if lista[x] < lista[x-1]:
        pico_vale.append('vale')
    else:
        pico_vale.append('pico')
for x in range(1, n):
    if pico_vale[x] == pico_vale[x-1] or lista[x] == lista[x-1]:
        a += 1
if a == 0:
    print(1)
else:
    print(0)
