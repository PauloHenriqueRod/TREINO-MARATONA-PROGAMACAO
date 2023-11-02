from math import sqrt
pi = 3.141592653589793

def calcular_raio_circunscrito(a, b, c, pi):
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    r = (a * b * c) / (4 * area)

    return round(2*pi*r,2)

def calcular_distancia_entre_pontos(x1, y1, x2, y2):
    distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia


while True:
    try:
        x1, y1, x2, y2, x3, y3 = [float(n) for n in input().split()]
        a = calcular_distancia_entre_pontos(x1, y1, x2, y2)
        b = calcular_distancia_entre_pontos(x1, y1, x3, y3)
        c = calcular_distancia_entre_pontos(x2, y2, x3, y3)
        print(calcular_raio_circunscrito(a, b, c, pi=pi))
    except EOFError:
        break