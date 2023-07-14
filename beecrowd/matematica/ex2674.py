def eh_primo(N):
    if N == 1:
        return False
    if N == 0:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def supers(num):
    if not eh_primo(int(num)):
        return False
    for i in range(len(num)):
        if not eh_primo(int(num[i])):
            return False
    return True

while True:
    try:
        N = int(input())
        if supers(str(N)):
            print('Super')
        elif eh_primo(N=N):
            print('Primo')
        else:
            print('Nada')
    except EOFError:
        break