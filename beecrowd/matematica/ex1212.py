'''while True:
    x, y = [n for n in input().split()]
    if len(x)<len(y):
        val = len(x)
    else:
        val = len(y)
    if x=='0' and y == '0':
        break
    carrys = sum([1 for n in range(val) if (int(x[n]) + int(y[n])) > 9])
    if len(x)<len(y):
        if y[len(y)-len(x)] == '9' and (int(x[0]) + int(y[len(y)-len(x)])>10):
            carrys += 1
    if len(y)>len(x):

    if carrys == 0:
        print('No carry operation.')
    elif carrys == 1:
        print('1 carry operation.')
    else:
        print(f'{carrys} carry operations.')
'''