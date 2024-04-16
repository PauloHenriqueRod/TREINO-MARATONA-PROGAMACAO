def is_subsequence(s:str, t:str) -> bool:
    sol = 0
    x = 0
    y = len(s) - 1
    a = 0
    b = len(t) - 1
    while a <= b and x <= y:
        if s[x] == t[a]:
            sol += 1
            x += 1
        if s[y] == t[b] and a!=b:
            sol += 1
            y-=1
        a += 1
        b -= 1
    return sol>=len(s)