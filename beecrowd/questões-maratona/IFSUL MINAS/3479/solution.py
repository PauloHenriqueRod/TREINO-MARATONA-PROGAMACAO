dia, mes = [int(n) for n in input().split('/')]
if mes == 1:
    if dia <= 19:
        print('capricornio')
    else:
        print('aquario')
elif mes == 2:
    if dia <= 18:
        print('aquario')
    else:
        print('peixes')
elif mes == 3:
    if dia <= 20:
        print('peixes')
    else:
        print('aries')
elif mes == 4:
    if dia <= 20:
        print('aries')
    else:
        print('touro')
elif mes == 5:
    if dia <= 20:
        print('touro')
    else:
        print('gemeos')
elif mes == 6:
    if dia <= 20:
        print('gemeos')
    else:
        print('cancer')
elif mes == 7:
    if dia <= 22:
        print('cancer')
    else:
        print('leao')
elif mes == 8:
    if dia <= 22:
        print('leao')
    else:
        print('virgem')
elif mes == 9:
    if dia <= 22:
        print('virgem')
    else:
        print('libra')
elif mes == 10:
    if dia <= 22:
        print('libra')
    else:
        print('escorpiao')
elif mes == 11:
    if dia <= 21:
        print('escorpiao')
    else:
        print('sagitario')
elif mes == 12:
    if dia <= 21:
        print('sagitario')
    else:
        print('capricornio')