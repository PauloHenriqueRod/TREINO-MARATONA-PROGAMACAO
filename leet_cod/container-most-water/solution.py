def maxArea(alturas: list[int]) -> int:
    min_x = 0
    max_x = len(alturas) - 1
    max_area = 0
    while x1 <= x2:
        area = min(alturas[min_x], alturas[max_x])*max_x-min_x
        max_area = max(area, max_area)
        if alturas[min_x] < alturas[max_x]:
            min_x+=1
        else:
            max_x-=1
    return(max_area)