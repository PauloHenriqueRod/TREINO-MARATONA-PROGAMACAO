n = int(input())
for x in range(0, n):
    palavra = str(input())
    texto = list(palavra)
    texto2 = list()
    for x in range(0, len(texto)):
        if texto[x] in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
            texto[x] = chr(ord(texto[x]) + 3)
    for y in range(len(texto)-1, -1, -1):
        texto2 += texto[y]
    for z in range(int(len(texto2)/2), len(texto2)):
        texto2[z] = texto2[z] = chr(ord(texto2[z]) - 1)
    print(''.join(texto2))
