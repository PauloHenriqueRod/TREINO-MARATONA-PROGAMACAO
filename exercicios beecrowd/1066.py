    pares = 0
    impares = 0
    pos = 0
    neg = 0
    for i in range(0, 5):
        n = int(input())
        if n > 0:
            pos += 1
        if n < 0:
            neg += 1
        if (n % 2) != 0:
            impares += 1
        if (n % 2) == 0:
            pares += 1
    print(f'{pares} valor(es) par(es)')
    print(f'{impares} valor(es) impar(es)   ')
    print(f'{pos} valor(es) positivo(s)')
    print(f'{neg} valor(es) negativo(s)')
