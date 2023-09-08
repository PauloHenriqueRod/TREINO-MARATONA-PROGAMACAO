def removeDuplicates(nums: list[int]) -> int:
    nums[2:] = [nums[i] for i in range(2, len(nums)) if nums[i]!=nums[i-2]]
    return len(nums)

lista = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(lista))
print(lista)