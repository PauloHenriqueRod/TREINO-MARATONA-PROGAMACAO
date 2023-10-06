from math import ceil
while True:
    EV1, EV2, AT, D = [int(n) for n in input().split()]
    if EV1 == 0 and EV2 == 0 and AT == 0 and D == 0:
        break
    EV1 = ceil(EV1/D)
    EV2 = ceil(EV2/D)
    n = EV1 + EV2
    if AT == 3:
        x = EV1
        y = n
    else:
        x = 1 - ((6-AT)/(AT))**(EV1)
        y = 1 - ((6-AT)/(AT))**(n)
    resposta = round(100*x/y, 1)
    print(resposta)