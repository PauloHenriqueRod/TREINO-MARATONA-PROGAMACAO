from time import sleep
def trailingZeroes(n: int) -> int:
    x = 5
    total = 0
    while x <= n:
        total += n // x
        x *= 5
    return total

print(trailingZeroes(200))
