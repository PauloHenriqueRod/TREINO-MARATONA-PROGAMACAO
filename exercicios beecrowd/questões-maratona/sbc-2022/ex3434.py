n = int(input())
palavra = input()
palavra = palavra.split('b')
print(sum([len(i) for i in palavra if len(i)>1]))
