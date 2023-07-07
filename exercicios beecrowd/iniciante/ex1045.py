x, y = [float(n) for n in input().split()]
if x == 0:
    if y == 0:
        print("Origem")
    else:
        print("Eixo Y")
if y == 0:
    if x != 0:
        print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
if y > 0:
    if x < 0:
        print('Q2')
if y < 0:
    if x < 0:
        print('Q3')
