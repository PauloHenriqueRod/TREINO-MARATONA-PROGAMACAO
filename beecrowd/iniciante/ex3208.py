'''while True:
    x, y = [int(x) for x in input().split()]
    if x == 0 and y == 0:
        break
    good = True
    for a in range(2, x,2):
        if (x % a) == 0:
            divisor = a
            break
        if a > y:
            divisor = y + 1
            break
    if divisor < y:
        print(f'BAD {divisor}')
    else:
        print(f'GOOD')
'''