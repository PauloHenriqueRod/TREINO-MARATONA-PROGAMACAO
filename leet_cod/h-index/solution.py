def hIndex(citations: list[int]) -> int:
    for i in range(len(citations), -1, -1):
        y = 0
        for j in citations:
            if j>=i:
                y+=1
            if y == i:
                return y
    return 0

print(hIndex([1,3,1]))