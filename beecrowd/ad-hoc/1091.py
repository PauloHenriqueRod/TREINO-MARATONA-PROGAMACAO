while True:
    k = int(input())
    if k == 0:
        break
    x, y = [int(n) for n in input().split()]
    for i in range(k):
        xlinha, ylinha = [int(n) for n in input().split()]
        xlinha = xlinha - x
        ylinha = ylinha - y
        if xlinha == 0 or ylinha == 0:
            print('divisa')
            continue
        elif xlinha > 0:
            if ylinha > 0:
                print('NE')
                continue
            else:
                print('SE')
                continue
        else:
            if ylinha > 0:
                print('NO')
                continue
            else:
                print('SO')
