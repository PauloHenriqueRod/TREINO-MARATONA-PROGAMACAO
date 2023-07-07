n = int(input())
for i in range(n):
    minuto, tempo = [n for n in input().split()]
    if '1' in tempo:
        if int(minuto) <= 45:
            print(minuto)
        else:
            acres = int(minuto) - 45
            print(f'{45}+{acres}')
    else:
        if int(minuto) <= 45:
            print(int(minuto)+45)
        else:
            acres = int(minuto) - 45
            print(f'90+{acres}')
