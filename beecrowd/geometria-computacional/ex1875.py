n = int(input())
for i in range(n):
    lista_gols = {'blue': 0, 'green': 0, 'red': 0}
    a = int(input())
    for j in range(a):
        x,y = [k.lower() for k in input().split()]
        if x == 'b':
            if y == 'r':
                lista_gols['blue'] += 2
                continue
            lista_gols['blue'] += 1
            continue
        if x == 'r':
            if y == 'b':
                lista_gols['red'] += 1
                continue
            lista_gols['red'] += 2
            continue
        if y == 'b':
            lista_gols['green'] += 2
            continue
        lista_gols['green'] += 1
    if lista_gols['blue'] == lista_gols['green'] == lista_gols['red']:
        print('trempate')
        continue
    if lista_gols['blue'] > lista_gols['green'] and lista_gols['blue'] > lista_gols['red']:
        print('blue')
        continue
    if lista_gols['green'] > lista_gols['blue'] and lista_gols['green'] > lista_gols['red']:
        print('green')
        continue
    if lista_gols['red'] > lista_gols['blue'] and lista_gols['red'] > lista_gols['green']:
        print('red')
        continue
    print('empate')