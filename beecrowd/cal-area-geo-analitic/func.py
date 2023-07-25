def calc_area(cords: list[list[int]]) -> float:
    area = 0
    for i in range(len(cords)-1):
        area += cords[i][0]*cords[i+1][1]
        area -= cords[i][1]*cords[i+1][0]
        print(area)
    area += cords[len(cords)-1][0]*cords[0][1]
    area -= cords[len(cords)-1][1]*cords[0][0]
    return abs(area/2)

print(calc_area([[50, 100], [250,250], [400, 150], [300, 0]]))
