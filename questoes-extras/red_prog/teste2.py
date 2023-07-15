lista = []
nomes = []
n = int(input())
for i in range(n):
    nome = input()
    if nome not in nomes:
        lista.append({'Nome': nome, 'Votos': 1})
        nomes.append(nome)
    else:
        lista[nomes.index(nome)]['Votos'] += 1

lista.sort(key=lambda d : d['Nome'])
if max(lista, key=lambda d : d['Votos'])['Votos'] > n/2:
    print(len(lista)-1)
    for x in range(len(lista)-1):
        print(lista[x]['Nome'])

else:
    minimo = min(lista, key=lambda d : d['Votos'])['Votos']
    print(sum([1 for x in lista if x['Votos'] == minimo]))
    for x in lista:
        if x['Votos'] == minimo:
            print(x['Nome'])
    