# Link questão: https://codeforces.com/problemset/problem/1199/B
h, l = [int(n) for n in input().split()]
result = (pow(l,2) - pow(h,2))/(2*h)
print(result)