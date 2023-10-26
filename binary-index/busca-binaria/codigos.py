def busca_binaria(lista: list, num: int):
    inicio = 0
    fim = len(lista) - 1
    while True:
        meio = (inicio+fim)//2
        if num == lista[meio]:
            return meio
        if inicio > fim:
            return - 1
        if num < lista[meio]:
            fim = meio-1
        else:
            inicio = meio+1


lista = [1,4,5,2,8,19,12,7,11,20,99,35,100]
lista.sort()
while True:
    x = int(input())
    print(lista)
    print(busca_binaria(lista=lista, num=x))
