n = int(input())
print(n)
while n>7:
    if n < 10:
        break
    n = (n//10)*3 + n%10
    print(n)