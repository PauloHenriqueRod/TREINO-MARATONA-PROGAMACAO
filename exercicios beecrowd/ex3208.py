while True:
    x, y = [int(x) for x in input().split()]
    if x == 0 and y == 0:
        break
    for a in range(2, x):
        if (x % a) == 0:
            divisor = a
            break
    if divisor < y:
        print(f'BAD {divisor}')
    else:
        print(f'GOOD')
