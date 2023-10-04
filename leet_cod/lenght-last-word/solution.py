def lengthOfLastWord(s: str) -> int:
        tam = 0
        if len(s) == 0:
                return 0
        i = len(s) - 1
        while s[i] == ' ':
                i -= 1
                if i == -1:
                       return 0
        while s[i] != ' ':
                print('chegou')
                tam+=1
                if i == 0:
                    return tam
                i-=1
        return tam

print(lengthOfLastWord('a '))