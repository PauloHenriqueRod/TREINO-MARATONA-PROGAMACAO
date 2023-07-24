'''
QUESTÃO COM TIME LIMITE ERROR

while True:
    lista = list(map(int, input().split()))
    if lista == [0]:
        break

    a = lista.pop(0)
    qts = sum(idx for idx, i in enumerate(lista, 1) if i != 0)
    
    if qts % 2 == 0:
        print('Carlos')
    else:
        print('Marcelo')
        
    '''