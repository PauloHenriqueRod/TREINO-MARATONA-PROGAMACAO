def longestPalindrome(s: str) -> int:
    palavras_sett = set(s)
    cont = 0
    impar = False
    for letra in palavras_sett:
        quant = s.count(letra)
        if s.count(letra)%2 == 0:
            cont += quant
        else:
            impar = True
            if quant == 1:
                continue
            else:
                cont += quant - 1
    return cont if not impar else cont + 1
print(longestPalindrome('a'))