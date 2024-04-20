x,y,z = [int(n) for n in input().split()]
if x**2 == y**2 + z**2:
    print(f"AREA = {(y*z)/2 + (3*(z/2)**2)/2:.0f}")
else:
    print("Nao eh retangulo!")