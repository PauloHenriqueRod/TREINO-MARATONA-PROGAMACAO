def canJump(nums: list[int]) -> bool:
    if len(nums) == 0 or len(nums)==1:
        return True
    maximo = 0
    tot = len(nums)
    for j, i in enumerate(nums):
        maximo = max(maximo, i)
        if i == 0:
            if maximo == 0:
                return False
        if maximo >= tot - j-1:
            return True
        maximo -= 1
    return True
        

print(canJump([2,0,0]))