from time import sleep
from math import ceil
def peakIndexInMountainArray(arr: list[int]) -> int:
    j = int((len(arr) - 1)/2)
    i = ceil(j/2)
    while True:
        print(j)
        if arr[j]>arr[j+1] and arr[j]>arr[j-1]:
            return j
        if arr[j-1]<arr[j]<arr[j+1]:
            j+=i
        else:
            j-=i
        i = ceil(i/2)

        


print(peakIndexInMountainArray([3,4,5,1]))