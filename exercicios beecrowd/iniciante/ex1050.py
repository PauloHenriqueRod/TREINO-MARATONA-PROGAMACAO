ddd = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro',
       32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}
n = int(input())
tot = 0
if n not in ddd.keys():
    print('DDD nao cadastrado')

for c, v in ddd.items():
    if n == c:
        print(f'{v}')
