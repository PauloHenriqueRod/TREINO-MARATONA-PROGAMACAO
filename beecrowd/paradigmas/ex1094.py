while True:
    n, d = [int(x) for x in input().split()]
    if n==0 and d==0:
        break
    num = input()
    num_final = []
    for i in num:
        while(len(num_final) > 0 or i > num_final[len(num_final)] and d > 0):
            num_final.pop()
            d-=1
        num_final.append(i)
    print(num_final)

