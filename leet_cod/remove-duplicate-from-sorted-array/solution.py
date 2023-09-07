def removeDuplicates(nums: list[int]) -> int:
    nums[1:] = [nums[i] for i in range(1, len(nums)) if nums[i]!=nums[i-1]]
    return len(nums)

lista = [1,1,1,1,1,1]
print(removeDuplicates(lista))
print(lista)