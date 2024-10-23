# Dada una lista de numeros, devolver los pares, devolver los impares


def pares_impares(nums):
    p=[]
    i=[]
    for n in nums:
        if n % 2 ==0:
            p.append(n)
        else:
            i.append(n)
    return p, i

#Programa principal

import os; os.system("cls")

nums = [9,8,60,6,90,7,10,6,7]
pares, impares = pares_impares(nums)

print("Numeros ", nums, len(nums))
print("Los pares son   : ", pares, len(pares))
print("Los impares son : ", impares, len(impares))
