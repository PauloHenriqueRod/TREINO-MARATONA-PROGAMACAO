jogo = input()
if jogo.count('O') > 1 or jogo.count('O') == 0:
    print('?')
elif 'XX' in jogo:
    print('Alice')
else:
    print('*')