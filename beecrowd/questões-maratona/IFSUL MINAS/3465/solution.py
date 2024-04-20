def area_triangulo(a,b,c):
    """
    Área do triângulo dado os lados
    """
    p = (a+b+c)/2
    area = ((p-a)*(p-b)*(p-c)*p)**(1/2)
    print(f"{area:.3f} m2")

a,b,c = [float(n) for n in input().split()]
area_triangulo(a,b,c)

