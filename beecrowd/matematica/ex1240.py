n = int(input())
for n in range(n):
    x, y = [int(n) for n in input().split()]
    if x % 10 ** (len(str(y))) == y:
        print('encaixa')
        continue
    print('nao encaixa')