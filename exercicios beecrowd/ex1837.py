x ,y = [int(n) for n in input().split()]
if x == 0:
    inteiro = 0
    resto = 0
elif x>0 and y>0:
    inteiro = x//y
    resto = x%y
elif x<0 and y<0:
    x = -1*x
    y = -1*y
    inteiro = x//y
    resto = x%y
elif x<0 and y>0:
    x = -1*x
    y = y
    inteiro = -1*(x//y)
    resto = x%y
elif x>0 and y<0:
    x = x
    y = -1*y
    inteiro = -1*(x//y)
    resto = x%y
print(f'{inteiro} {resto}')
