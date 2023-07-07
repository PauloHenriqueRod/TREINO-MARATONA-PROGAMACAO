num = int(input())
for x in range(num):
    texto = input()
    if texto == 'P=NP':
        print('skipped')
    else:
        print(eval(texto))
