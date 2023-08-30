n = input()
joao = [int(n) for n in input().split()]
maria = [int(n) for n in input().split()]
cartas = [int(n) for n in input().split()]
val_joao = sum([n if n <=10 else 10 for n in joao])
val_maria = sum([n if n <=10 else 10 for n in maria])
val_cartas = sum([n if n <=10 else 10 for n in cartas])
resposta = -1
if val_joao<=val_maria:
    valor = 23-val_maria - val_cartas
    if valor > 10:
        resposta = -1
    elif valor<10:
        if joao.count(valor) + maria.count(valor) + cartas.count(valor) < 4:
            resposta = valor
    else:
        for i in range(10, 14):
            if joao.count(i) + maria.count(i) + cartas.count(i) < 4:
                resposta = i        
                break
else:
    min_possivel = 23 - (val_joao + val_cartas)
    valor_joao = val_joao + val_cartas
    valor_maria = val_maria + val_cartas
    if min_possivel>10:
        resposta = -1
    else:
        for i in range(min_possivel+1, 14):
                if i <= 10:
                    if valor_maria + i > 23:
                        break
                    if joao.count(i) + maria.count(i) + cartas.count(i) < 4:
                        resposta = i        
                        break
                else:
                    if valor_maria + 10 > 23:
                        break
                    if joao.count(i) + maria.count(i) + cartas.count(i) < 4:
                        resposta = i        
                        break
if resposta > 10:
    print(-1)
else:
    print(resposta)