def rotate(nums: list[int], k: int) -> None:
    x = len(nums)
    if k>=x:
        k = k % x
    aux = nums[-k:]
    nums[k:] = nums[:-k]
    nums[:k] = aux
