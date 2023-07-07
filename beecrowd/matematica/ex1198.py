while True:
    try:
        a, b = [int(n) for n in input().split()]
        if a < b:
            print(b - a)
        else:
            print(a - b)
    except EOFError:
        break
