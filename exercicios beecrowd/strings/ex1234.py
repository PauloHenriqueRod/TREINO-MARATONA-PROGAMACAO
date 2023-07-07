while True:
    try:
        sentenca = input()
        sentenca_transf = ''
        aux = 0
        for x in range(0, len(sentenca)):
            if sentenca[x].isalpha():
                if aux % 2 == 0:
                    sentenca_transf += sentenca[x].upper()
                    aux += 1
                else:
                    sentenca_transf += sentenca[x].lower()
                    aux += 1
            else:
                sentenca_transf += sentenca[x]
                continue
        print(sentenca_transf)
    except EOFError:
        break
