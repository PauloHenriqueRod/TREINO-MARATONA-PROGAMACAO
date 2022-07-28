lista = ['---', '--*', '-*-', '-**', '*--', '*-*', '**-', '***']
for c in range(0, 3):
    soma = 0
    while True:
        y = str(input())
        if y != 'caw caw':
            soma += lista.index(y)
        if y == 'caw caw':
            break
    print(soma)
