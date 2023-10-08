from math import ceil
def ruina_do_jogador(inicio, sucesso, p, quant):
    q = 1 - p
    sucesso = ceil(sucesso/quant)
    inicio = ceil(inicio/quant)
    if p == q:
        x = inicio
        y = sucesso
    else:
        x = 1 - (q/p)**(inicio)
        y = 1 - (q/p)**sucesso
    return round(100*x/y, 1)


while True:
    EV1, EV2, AT, D = [int(n) for n in input().split()]
    if EV1 == 0 and EV2 == 0:
        break
    sucesso = EV1 + ceil(EV2/D)*D
    resp = ruina_do_jogador(EV1, sucesso,AT/6,D)
    print(resp)