x1, y1 = [float(n) for n in input().split()]
x2, y2 = [float(n) for n in input().split()]
distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print(f"{distancia:.4f}")
