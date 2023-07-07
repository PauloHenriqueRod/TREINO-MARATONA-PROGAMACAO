while True:
    try:
        bix = 0
        aux = 0
        ano = int(input())
        if ano % 400 == 0:
            bix += 1
        elif ano % 4 == 0 and ano % 100 != 0:
            bix += 1
        if bix != 0:
            print('This is leap year.')
            aux += 1
        if ano % 15 == 0:
            print('This is huluculu festival year.')
            aux += 1
        if ano % 55 == 0 and bix != 0:
            print('This is bulukulu festival year.')
            aux += 1
        if aux == 0:
            print('This is an ordinary year.')q
    except EOFError:
        break
