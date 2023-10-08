idades = [int(n) for n in input().split()]
copia = idades.copy()
copia.remove(max(idades))
copia.remove(min(idades))
nomes = ['huguinho', 'zezinho', 'luisinho']
print(nomes[idades.index(copia[0])])