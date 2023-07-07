def transf_volta(volta):
    lista_volta = volta.split(':')
    volta_final = 0
    minutos = int(lista_volta[0]) * 60000
    segundos = int(lista_volta[1]) * 1000
    milissegundos = int(lista_volta[2])
    volta_final = minutos + segundos + milissegundos
    return volta_final


pilot, volts = [int(n) for n in input().split()]
pilotos = []
voltas_rapidas = []
qual_volta = []
qual_volta_rapido = []
piloto_rapido = []
posicao_pilotos = []
tempos_totais = []
voltas = []
voltasmaisrapidas = []

for x in range(pilot):
    volta_piloto = []
    a = input().split()
    for i in range(volts+1):
        if i == 0:
            pilotos.append(int(a[i]))
        else:
            volta_piloto.append(transf_volta(a[i]))
    voltas.append(volta_piloto)
    total_tempo = sum(volta_piloto)
    voltas_rapidas.append(min(volta_piloto))
    qual_volta.append(volta_piloto.index(min(volta_piloto)))
    tempos_totais.append(total_tempo)

for x, piloto in enumerate(pilotos):
    if voltas_rapidas[x] == min(voltas_rapidas) and tempos_totais[x] <= sorted(tempos_totais)[9]:
        piloto_rapido.append(piloto)
        qual_volta_rapido.append(qual_volta[x])
        voltasmaisrapidas.append(voltas[x])

qual_volta_rapido_ordenado = sorted(qual_volta_rapido)

if len(piloto_rapido) == 1:
    print(piloto_rapido[0])
elif len(piloto_rapido) == 0:
    print('NENHUM')
else:
    for x, piloto in enumerate(piloto_rapido):
        if qual_volta_rapido[x] != qual_volta_rapido_ordenado[0]:
            piloto_rapido.pop(x)
    if len(piloto_rapido) == 1:
        print(piloto_rapido[0])
    else:
        menor_volta = qual_volta_rapido_ordenado[0]
        mais_rapido = 0
        voltamenor = sum(voltasmaisrapidas[0][:menor_volta])

        for x, piloto in enumerate(piloto_rapido):
            soma_voltas = sum(voltasmaisrapidas[x][:menor_volta])
            if soma_voltas < voltamenor:
                mais_rapido = x
                voltamenor = soma_voltas

        print(piloto_rapido[mais_rapido])