from math import floor
n = int(input())
m = int(input())

x = int(floor((m-n*2)/2))
if n == floor(m/2):
    print('Amelia tem todas bolinhas!')
else:
    print(f'Faltam {x} bolinha(s)')