def reverseWords(s: str) -> str:
    palavras = s.split()
    palavras.reverse()
    return " ".join(palavras)

lista = "the sky is blue"
print(reverseWords(lista))