def calcular_mdc(numero1, numero2): # Algoritmo de Euclides
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1

while True:
    try:
        nums = [int(n) for n in input().split()]
        nums.sort()
        if nums[2]**2 != nums[0]**2 + nums[1]**2:
            print('tripla')
        else:
            if calcular_mdc(numero1=calcular_mdc(numero1=nums[1], numero2=nums[0]),numero2=nums[2]) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
    except EOFError:
        break