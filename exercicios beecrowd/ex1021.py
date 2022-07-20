n = float(input())
nint = int(n)
nmoeda = (n - nint)*100
cem = 0
cinq = 0
vint = 0
dez = 0
cinc = 0
dois = 0
um = 0
cinqmoed = 0
vintcinmoed = 0
dezmoed = 0
cincmoed = 0
uncents = 0
while n >= 100:
    cem += 1
    n -= 100
while n >= 50:
    cinq += 1
    n -= 50
while n >= 20:
    vint += 1
    n -= 20
while n >= 10:
    dez += 1
    n -= 10
while n >= 5:
    cinc += 1
    n -= 5
while n >= 2:
    dois += 1
    n -= 2
while n >= 1:
    um += 1
    n -= 1
while nmoeda >= 50:
    cinqmoed += 1
    nmoeda -= 50
while nmoeda >= 25:
    vintcinmoed += 1
    nmoeda -= 25
while nmoeda >= 10:
    dezmoed += 1
    nmoeda -= 10
while nmoeda >= 5:
    cincmoed += 1
    nmoeda -= 5
while nmoeda >= 1:
    uncents += 1
    nmoeda -= 1
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(cem))
print('{} nota(s) de R$ 50.00'.format(cinq))
print('{} nota(s) de R$ 20.00'.format(vint))
print('{} nota(s) de R$ 10.00'.format(dez))
print('{} nota(s) de R$ 5.00'.format(cinc))
print('{} nota(s) de R$ 2.00'.format(dois))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(um))
print('{} moeda(s) de R$ 0.50'.format(cinqmoed))
print('{} moeda(s) de R$ 0.25'.format(vintcinmoed))
print('{} moeda(s) de R$ 0.10'.format(dezmoed))
print('{} moeda(s) de R$ 0.05'.format(cincmoed))
print('{} moeda(s) de R$ 0.01'.format(uncents))
