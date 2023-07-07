while True:
    try:
        R1, X1, Y1, R2, X2, Y2 = [int(n) for n in input().split()]
        if R2 > R1:
            print("MORTO")
        else:
            diferenca_centros = ((X1-X2)**2 + (Y1-Y2)**2)**(1/2)
            diferenca_raios = R1 - R2
            if diferenca_centros <= diferenca_raios:
                print("RICO")
            else:
                print("MORTO")
    except:
        break
