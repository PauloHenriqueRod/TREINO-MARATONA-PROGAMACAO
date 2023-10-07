lista = {"SP": 2, "PR": 1, "SC": 1, "MG": 1, "RJ": 1, "RS": 1, "PE": 1}
estado = input()
if estado in lista:
    print(lista[estado])
else:
    print(0)
