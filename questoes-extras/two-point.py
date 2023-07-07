def dois_pontos(target:int, lista: list):
    lista_ordenada = sorted(lista)
    i = 0
    j = len(lista) - 1
    while i!=j:
        soma = lista_ordenada[i] + lista_ordenada[j]
        if soma == target:
            if lista_ordenada[i] == lista_ordenada[j]:
                return [lista.index(lista_ordenada[i]), len(lista) - lista[::-1].index(lista_ordenada[j])]
            return [lista.index(lista_ordenada[i]), lista.index(lista_ordenada[j])]
        elif soma < target:
            i+=1
        else:
            j-=1
