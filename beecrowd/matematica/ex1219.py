from math import pi
def area_triangulo(a,b,c):
    """
    Área do triângulo dado os lados
    """
    p = (a+b+c)/2
    area = ((p-a)*(p-b)*(p-c)*p)**(1/2)
    return area

def circulo_circuinscrito(a,b,c,pi):
    p = (a+b+c)/2
    areaT = ((p-a)*(p-b)*(p-c)*p)**(1/2)
    R = (a*b*c)/(4*areaT)
    return pi*(R**2)

def circulo_inscrito(a,b,c,pi):
    p = (a+b+c)/2
    areaT = ((p-a)*(p-b)*(p-c)*p)**(1/2)
    r = areaT/p
    return pi*(r**2)

while True:
    try:
        x,y,z = [int(n) for n in input().split()]
        area_rosas = circulo_inscrito(x,y,z, pi=pi)
        area_violetas = area_triangulo(x,y,z) - area_rosas
        area_girassois = circulo_circuinscrito(x,y,z,pi=pi) - area_violetas - area_rosas
        print(f'{area_girassois:.4f} {area_violetas:.4f} {area_rosas:.4f}')
    except EOFError:
        break
