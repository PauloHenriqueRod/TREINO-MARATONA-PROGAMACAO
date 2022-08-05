n = int(input())
for p in range(1, n+1):
    x, y = [x for x in input().split()]
    if x == y:
        print(f'Caso #{p}: De novo!')
    else:
        if x == 'tesoura':
            if y == 'papel' or y == 'lagarto':
                print(f'Caso #{p}: Bazinga!')
            else:
                print(f'Caso #{p}: Raj trapaceou!')
        if x == 'papel':
            if y == 'pedra' or y == 'Spock':
                print(f'Caso #{p}: Bazinga!')
            else:
                print(f'Caso #{p}: Raj trapaceou!')
        if x == 'lagarto':
            if y == 'Spock' or y == 'papel':
                print(f'Caso #{p}: Bazinga!')
            else:
                print(f'Caso #{p}: Raj trapaceou!')
        if x == 'Spock':
            if y == 'tesoura' or y == 'pedra':
                print(f'Caso #{p}: Bazinga!')
            else:
                print(f'Caso #{p}: Raj trapaceou!')
        if x == 'pedra':
            if y == 'tesoura' or y == 'lagarto':
                print(f'Caso #{p}: Bazinga!')
            if y == 'Spock' or y == 'papel':
                print(f'Caso #{p}: Raj trapaceou!')
