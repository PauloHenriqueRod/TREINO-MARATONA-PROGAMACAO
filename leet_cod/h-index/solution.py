def hIndex(citations: list[int]) -> int:
    citations.sort()
    tam = len(citations)
    for i in range(0, tam):
        if citations[i] >= tam-i:
            print(citations[i])
            return tam-i
    return 0

print(hIndex([3,0,6,1,5]))