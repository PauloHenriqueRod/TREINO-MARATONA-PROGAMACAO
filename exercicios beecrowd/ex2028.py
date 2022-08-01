x = 1
while True:
    lista = [0]
    y = 1
    try:
        n = int(input())
        for a in range(0, n):
            for b in range(0, a+1):
                lista.append(a+1)
                y += 1
        if n == 0:
            print('Caso 1: 1 numero')
        else:
            print(f'Caso {x}: {y} numeros')
        x += 1
        for c in range(0, len(lista)):
            if c == len(lista) - 1:
                print(f'{lista[c]}')
            else:
                print(f'{lista[c]}', end=' ')
        print()
        lista.clear()
    except EOFError:
        break
