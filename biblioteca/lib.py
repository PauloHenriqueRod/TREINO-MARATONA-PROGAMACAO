from math import ceil

def ruina_do_jogador(inicio: int, sucesso:int, p:float, quant: int) -> float:
    """
    inicio = quantidade incial do jogador
    sucesso = quantia que simboliza o sucesso
    p = chances de ganhar
    quant = quantidade que perde/ganha por rodada
    utiliza a função CEIL da biblioteca MATH
    """
    q = 1 - p # Probabilidade de fracasso
    sucesso = ceil(sucesso/quant) # Mudando a escala
    inicio = ceil(inicio/quant) # Mudando a escala
    if p == q:
        x = inicio
        y = sucesso
    else:
        x = 1 - (q/p)**(inicio)
        y = 1 - (q/p)**sucesso
    return round(100*x/y, 1)

def calcular_mdc(numero1, numero2): # Algoritmo de Euclides
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1