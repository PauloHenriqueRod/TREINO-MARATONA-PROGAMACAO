x, y = [int(n) for n in input().split()]
assuntos = []
for i in range(x):
    mat = [int(n) for n in input().split()]
    assuntos.append(mat)
aluno = [int(n) for n in input().split()]
for i in range(x):
    print(sum([abs(aluno[j]-assuntos[i][j]) for j in range(y)]))