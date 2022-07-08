A, B, C, D = [int(n) for n in input().split()]
check = 0
if B > C:
    check += 1
if D > A:
    check += 1
if (C + D) > (A+B):
    check += 1
if C > 0 and D > 0:
    check += 1
if A % 2 == 0:
    check += 1
if check == 5:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
