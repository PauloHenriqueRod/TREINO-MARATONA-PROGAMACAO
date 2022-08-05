lista_fontes = {'suco de laranja': int(120), 'morango fresco': int(85), 'mamao': int(85),
                'goiaba vermelha': int(70), 'manga': int(56), 'laranja': int(50), 'brocolis': int(34)}
while True:
    vitc = 0
    n = int(input())
    if n == 0:
        break
    for x in range(n):
        resp = input().split()
        qt = int(resp[0])
        fonte = ' '.join(resp[1:])
        vitc += qt*lista_fontes[fonte]
    if vitc > 130:
        print(f'Menos {vitc-130} mg')
    elif vitc < 110:
        print(f'Mais {110-vitc} mg')
    else:
        print(f'{vitc} mg')
