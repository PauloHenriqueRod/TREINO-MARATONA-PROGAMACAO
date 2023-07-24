vogal = 'aeiou'
palavra = input()
resp = 1
for x in range(len(palavra)-1):
    if palavra[x] in vogal and palavra[x+1] in vogal:
        resp = 0
        break
    if palavra[x] not in vogal and palavra[x+1] not in vogal:
        resp = 0
        break
print(resp)
