while True:
    x, y = [n for n in input().split()]
    if int(x) == 0 and int(y) == 0:
        break
    x_lista = list(x)
    y_lista = list(y)
    tot = 0
    x_int = list(map(lambda c: int(c), x_lista))
    y_int = list(map(lambda b: int(b), y_lista))
    if len(x_int) >= len(y_int):
        aux = 0
        for t in range(len(y_lista)-1, -1, -1):
            a = x_int[t] + y_int[t] + aux
            if a >= 10:
                tot += 1
                aux = 1
            else:
                aux = 0
    else:
        aux = 0
        for t in range(len(x_lista) - 1, -1, -1):
            a = x_int[t] + y_int[t] + aux
            if a >= 10:
                tot += 1
                aux = 1
            else:
                aux = 0
    if tot == 0:
        print('No carry operation.')
    elif tot == 1:
        print(f'{tot} carry operation.')
    else:
        print(f'{tot} carry operations.')
