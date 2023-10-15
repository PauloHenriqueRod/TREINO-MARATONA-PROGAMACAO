from time import sleep

while True:
    try:
        n = int(input())
        x = 1
        resto = 1 % n
        while resto != 0:
            sleep(0.5)
            print(resto)
            resto = (resto * 10 + 1) % n
            x += 1
        print(x)
    except EOFError:
        break