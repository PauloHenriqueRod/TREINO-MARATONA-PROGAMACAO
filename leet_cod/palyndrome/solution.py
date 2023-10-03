def isPalindrome(s: str) -> bool:
    x = 0
    y = len(s) - 1
    while True:
        while True:
            if x == y or y<x:
                return True
            if s[x].isalpha() or s[y].isnumeric():
                break
            x+=1
        while True:
            if x == y or y<x:
                return True
            if s[y].isalpha() or s[y].isnumeric():
                break
            y-=1
        if s[x].lower() != s[y].lower():
            print(f'{s[x]} ---- {s[y]}')
            return False
        if x == y or y<x:
            return True
        x+=1
        y-=1
            
print(isPalindrome("0P"))