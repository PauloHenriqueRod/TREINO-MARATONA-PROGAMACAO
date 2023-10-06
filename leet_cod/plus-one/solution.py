def plusOne(digits: list[int]) -> list[int]:
    lista = []
    soma_um = True
    for i in range(len(digits)-1, -1, -1):
        if soma_um:
            x = digits[i] + 1
            if x==10:
                lista.append(0)
            else:
                lista.append(x)
                soma_um = False
        else:
            lista.append(digits[i])
    if soma_um:
        lista.append(1)
    lista.reverse()
    return(lista)

print(plusOne([9, 0, 9]))