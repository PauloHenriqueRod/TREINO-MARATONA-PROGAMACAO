def remove_element(nums: list[int], val: int) ->int:
    tam = len(nums)
    nums[:] = [i for i in nums if i !=val]
    k = len(nums)
    return k
lista = [0,1,2,2,3,0,4,2]
print(remove_element(lista, 2))
print(lista)


