x, y = [int(n) for n in input().split()]
matriz = []
for i in range(x):
    matriz.append([int(n) for n in input().split()])
certo = True
linha_coluna = []
matriz_aux = []

for i in range(x):
    matriz_2 = []
    for j in range(y):
        matriz_2.append(0)
    matriz_aux.append(matriz_2)
total = 0
for i in range(x-1):
    for j in range(y-1):
        if matriz[i][j] == 1:
            if matriz_aux[i][j] == 0:
                matriz_aux[i][j] = 1
                matriz_aux[i][j+1] = 1
                matriz_aux[i+1][j] = 1
                matriz_aux [i+1][j+1] = 1
                if matriz[i][j+1] == 1 and matriz[i+1][j] == 1 and matriz[i+1][j+1] == 1:
                    linha_coluna.append([i+1, j+1])
                    total += 1
                else:
                    certo = False
                    break
            else:
                if matriz[i][j+1] == 1 and matriz[i+1][j] == 1 and matriz[i+1][j+1] == 1:
                    matriz_aux[i][j] = 1
                    matriz_aux[i][j+1] = 1
                    matriz_aux[i+1][j] = 1
                    matriz_aux [i+1][j+1] = 1
                    total += 1
                    linha_coluna.append([i+1, j+1])
if not certo or (matriz != matriz_aux):
    print(-1)
else:
    print(total)
    for i in linha_coluna:
        print(i[0], i[1])