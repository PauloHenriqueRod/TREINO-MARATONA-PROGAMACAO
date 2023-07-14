while True:
    x, y = [n for n in input().split()]
    if len(x)<len(y):
        val = len(x)
    else:
        val = len(y)
    if x=='0' and y == '0':
        break
    x = x.zfill(9)
    y = y.zfill(9)
    carrys = 0
    aux = 0
    for i in range(8, -1, -1):
        if int(x[i]) + int(y[i]) + aux > 9:
            carrys += 1
            aux = 1
        else:
            aux = 0
    if carrys == 0:
        print('No carry operation.')
    elif carrys == 1:
        print('1 carry operation.')
    else:
        print(f'{carrys} carry operations.')
