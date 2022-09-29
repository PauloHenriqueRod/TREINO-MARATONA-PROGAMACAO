n = int(input())
for x in range(n):
    frase = input()
    lista_frase = []
    for a in range(len(frase)):
        if not frase[a].isalpha():
            continue
        else:
            if frase[a] in lista_frase:
                continue
            else:
                lista_frase.append(frase[a])
    if len(lista_frase) == 26:
        print('frase completa')
    elif len(lista_frase) >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
