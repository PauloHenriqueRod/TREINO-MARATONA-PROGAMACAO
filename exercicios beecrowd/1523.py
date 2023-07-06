while True:
    mots, maxs = [int(n) for n in input().split()]
    lista = []
    if mots == 0 and maxs == 0:
        break
    possivel = True
    for x in range(mots):
        ent, said = [int(n) for n in input().split()]
        if len(lista) == 0:
            lista.append([ent, said])
        else:
            lista = [x for x in lista if x[1] > ent]
            try:
                if said > lista[len(lista)-1][1]:
                    possivel = False
                    lista.append([ent, said])
                else:
                    lista.append([ent, said])
            except:
                continue
            if len(lista) > maxs:
                possivel = False
    print('Sim' if possivel else 'Nao')
