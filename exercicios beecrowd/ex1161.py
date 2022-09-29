from math import factorial as fat
while True:
    try:
        x, y = [int(n) for n in input().split()]
        print(fat(x) + fat(y))
    except EOFError:
        break
