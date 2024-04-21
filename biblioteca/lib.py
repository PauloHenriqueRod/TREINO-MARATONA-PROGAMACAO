from math import ceil
import math

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

def calcular_mmc(numero1, numero2):
    x = calcular_mdc(numero1=numero1, numero2=numero2)
    return numero1*numero2 // x

def eh_primo(n): # Número primo ou não
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def contar_digitos(numero):
    """Função que conta o número de dígitos de um número inteiro"""
    if numero == 0:
        return 1

    quantidade_de_digitos = int(math.log10(abs(numero)) + 1)
    return quantidade_de_digitos


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
def wagner_fischer(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Inicializando a matriz de distância
    dist = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Inicializando a primeira coluna
    for i in range(1, m + 1):
        dist[i][0] = i
    
    # Inicializando a primeira linha
    for j in range(1, n + 1):
        dist[0][j] = j
    
    # Preenchendo a matriz de distância
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dist[i][j] = min(dist[i - 1][j] + 1,      # Deleção
                             dist[i][j - 1] + 1,      # Inserção
                             dist[i - 1][j - 1] + cost)  # Substituição ou match
    
    return dist[m][n]