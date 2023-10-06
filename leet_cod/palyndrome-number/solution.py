def solve(x: int):
    return str(str(x) == str(x)[::-1]).lower()

print(solve(-121))  