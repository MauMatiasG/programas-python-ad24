# Remover elementso de una lista de numeros

import os; os.system("cls")

nums = [1,3,5,7,9,11,99,15,88,19,100]
print("Remover elementos de una lista de numeros")
print("Los numeros : ", nums, len(nums))

print("Remover un numero (remueve la primera ocurrencia)")
nums.remove(99)
print("Queda : ", nums, len(nums))

print("Remover un elemento en una posicion determinada")
e = nums.pop(8)
print("Queda : ", nums, len(nums), e)

print("Remover el ultimo elemento de la lista")
e = nums.pop()
print("Queda : ", nums, len(nums), e)

print("Remover todos los elementos de la lista")
nums.clear()
print("Queda : ", nums, len(nums))