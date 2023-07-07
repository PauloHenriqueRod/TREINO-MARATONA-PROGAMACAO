num = int(input())
alunos = []
medias = []
for x in range(num):
    nome_aluno = input()
    nota_alunos = []
    a = input().split()
    for y in range(4):
        try:
            nota_alunos.append(float(a[y]))
        except:
            break
    if len(nota_alunos) == 1:
        nota_alunos.append(0)
    if len(nota_alunos) == 4:
        nota_alunos.remove(min(nota_alunos))
    alunos.append(nome_aluno)
    medias.append(sum(nota_alunos)/len(nota_alunos))
for x in range(len(alunos)):
    print(f"{alunos[x]}: {medias[x]:.1f}")
