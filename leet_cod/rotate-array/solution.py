def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    for i in range(len(nums) - k):
        x=nums.pop(0)
        nums.append(x)
