def hIndex(citations: list[int]) -> int:
    citations.sort()
    tam = len(citations)
    for i in range(0, tam):
        x = tam-i
        if citations[i] >= x:
            return x
    return 0

print(hIndex([3,0,6,1,5]))