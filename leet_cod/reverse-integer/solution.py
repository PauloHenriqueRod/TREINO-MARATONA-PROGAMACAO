def reverse(x:int) -> int:
    if x >= 0:
        result = int(str(x)[::-1])
    else:
        result = int(f'{"-"}{str(x)[:0:-1]}')
    if result > 2**(31) - 1 or result < -2**(31):
        return 0
    return result
print(reverse(321))