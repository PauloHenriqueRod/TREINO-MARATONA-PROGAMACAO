from math import floor
n = int(input())
for i in range(n):
    s = int(input())
    resposta = ((1+8*s)**(1/2) - 1)/2
    print(int(floor(resposta)))