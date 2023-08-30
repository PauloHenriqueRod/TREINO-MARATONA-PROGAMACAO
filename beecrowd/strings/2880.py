a = input()
b = input()
x = len(a)
y = len(b)
count = 0
for i in range(x-y+1):
    teste = True
    for j in range(i, y+i):
        if a[j] == b[j-i]:
            teste = False
            break
    if teste:
        count += 1
print(count)