while True:
    x1, y1, x2, y2 = [int(n) for n in input().split()]
    if x1==0 and x2 == 0 and y1 == 0 and y2==0:
        break
    if x1 == x2 and y1==y2:
        print(0)
        continue
    elif x1 == x2 or y1 == y2:
        print(1)
        continue
    elif abs(x1-x2) == abs(y1 - y2):
        print(1)
        continue
    else:
        print(2)
        continue