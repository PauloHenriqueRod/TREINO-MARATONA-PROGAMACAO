# Código traz resultados satisfatórios mas com TLE. Buscar aprimorar pra passar sem TLE
def multiplos(num: int, num2: int):
    i = 1
    multiplos = set()
    aux = num
    while aux < num2:
        aux = num*i
        if aux < num2:
            multiplos.add(aux)
        i += 1
    return multiplos

while True:
    t, x, y = [int(n) for n in input().split()]
    if t==0 and x == 0 and y == 0:
        break
    x = multiplos(x, t)
    y = multiplos(y, t)
    for a in range(1, t):
        if (t%a==0):
            if len(multiplos(a, t).intersection(x.intersection(y))) == 0:
                print(a, end=' ')
    print(t)

