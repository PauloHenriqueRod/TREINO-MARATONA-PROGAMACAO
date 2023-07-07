H, E, A, O, W, X = [int(n) for n in input().split()]
bem = H + E + A
mal = O + W
if bem > mal:
    print('Middle-earth is safe.')
else:
    bem += X
    if bem >= mal:
        print('Middle-earth is safe.')
    else:
        print('Sauron has returned.')
