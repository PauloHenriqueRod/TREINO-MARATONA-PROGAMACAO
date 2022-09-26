num = int(input())
for a in range(num):
    string = input()
    nova_palavra = ''
    for x in range(int(len(string)/2-1), -1, -1):
        nova_palavra += string[x]
    for x in range(len(string)-1, int(len(string)/2)-1, -1):
        nova_palavra += string[x]
    print(nova_palavra)
