def mmc_true(a, b, c, t):
    if a >= b and a >= c :
        maior = a
    elif b >= a and b >= c:
        maior = b
    else:
        maior = c
    for i in range(maior, t+1, maior):
        if i%a==0 and i%b==0 and i%c==0:
            if i == t:
                return True
            return False
    return False;

while True:
    x, y, z = [int(n) for n in input().split()]
    if x == 0 and y == 0 and z == 0:
        break
    inicio = int(x/(y*z))
    for i in range(inicio, (x//2)+1, inicio):
        if mmc_true(y,z,i,x):
            print(i, end=' ')
    print(x)