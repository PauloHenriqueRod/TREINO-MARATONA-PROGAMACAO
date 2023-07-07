N1, N2, N3, N4 = [float(n) for n in input().split()]
media = (N1*2+N2*3+N3*4+N4)/10
print(f"Media: {media:.1f}")
if media > 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    NEX = float(input())
    print(f"Nota do exame: {NEX:.1f}")
    media = (media+NEX)/2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print(f"Media final: {media:.1f}")
