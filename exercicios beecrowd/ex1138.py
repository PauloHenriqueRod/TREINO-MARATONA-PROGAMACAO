while True:
    num_frase = ''
    a, b = [int(n) for n in input().split()]
    if a == 0 and b == 0:
        break
    for x in range(a, b+1):
        num_frase += str(x)
    print(f'{num_frase.count("0")} {num_frase.count("1")} {num_frase.count("2")} '
          f'{num_frase.count("3")} {num_frase.count("4")} {num_frase.count("5")} '
          f'{num_frase.count("6")} {num_frase.count("7")} {num_frase.count("8")} '
          f'{num_frase.count("9")}')
print()
