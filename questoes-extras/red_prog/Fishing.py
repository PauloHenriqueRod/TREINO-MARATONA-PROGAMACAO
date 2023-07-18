def range_x(x1,s):
    return x1+s

def range_y(y1,s):
    return y1+s


def solve(s, cords, xis, yps):
    max = 0
    for x in range(xis):
        rangedox = range_x(x1=x, s=s)
        for y in range(yps):
            rangedoy = range_y(y1=y, s=s)
            aux = 0
            for a in cords:
                if (x <= a[0] <= rangedox) and (y <= a[1] <=rangedoy):
                    aux+=1
            if aux > max:
                max = aux
    return max


s, n = [int(n) for n in input().split()]
cordenadas = []
for i in range(n):
    x, y = [int(n) for n in input().split()]
    if [x, y] in cordenadas:
        continue
    cordenadas.append([x, y])

print(solve(s=s, cords=cordenadas, xis=100, yps=100))


