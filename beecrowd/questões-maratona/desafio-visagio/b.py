hashtag = input().strip()
quant = int(input())
tot = 0
procura = (f'#{hashtag}')
for x in range(quant):
    curso = input()
    lista = curso.split()
    if f'{procura} ' in curso or f'{procura}#'.lower() in curso:
        tot += 1
    elif curso.find(procura) == (len(curso) - len(procura)):
        tot += 1
    else:
        if curso[curso.find(procura) + len(procura)].isalpha():
            continue
        else:
            tot+=1
print(tot)