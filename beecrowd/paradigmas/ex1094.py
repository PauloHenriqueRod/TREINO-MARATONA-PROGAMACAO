while True:
    n, d = [int(x) for x in input().split()]
    if n==0 and d==0:
        break
    num = input()
    dlinha = d
    valor_final = 0
    indice = 0
    mult = n - d
    while dlinha>0:
        maioralgorismo = 0
        for i in range(indice, indice+dlinha+1):
            try:
                if int(num[i]) > maioralgorismo:
                    maioralgorismo = int(num[i])
                    indice = i
            except:
                continue
        dlinha-=indice
        indice+=1
        valor_final += int(maioralgorismo) * (10**(mult-1))
        mult = mult-1
    try:
        if mult!=0:
            valor_final+=int(num[indice:n])
    except:
        continue
    print(int(valor_final))


