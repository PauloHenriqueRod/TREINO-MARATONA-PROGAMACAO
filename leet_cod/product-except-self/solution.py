def productExceptSelf(nums: list[int]) -> list[int]:
    zero = False
    produto = 1
    nums_product = []
    x = nums.count(0)
    if x > 1:
        return [0]*len(nums)
    for x in nums:
        if x == 0:
            zero = True
            continue
        produto = produto*x
    if zero:           
        for i in range(len(nums)):
            if nums[i] == 0:
                nums_product.append(produto)
                continue
            nums_product.append(0)
    else:
        for i in range(len(nums)):
            nums_product.append(int(produto/nums[i]))
    return nums_product

print(productExceptSelf([0,4,0]))