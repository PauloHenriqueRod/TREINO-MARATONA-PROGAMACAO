while True:
    try:
        maior = 0
        n = int(input())
        x = input().split()
        for i in range(n):
            if int(x[i]) > maior:
                maior = int(x[i])
        if maior < 10:
            print(1)
        elif maior >= 20:
            print(3)
        else:
            print(2)
    except EOFError:
        break
