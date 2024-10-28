# Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
# Se crea una función que calcula el factorial de un número (ya la hicimos en clase)
#Se crea una función que recibe las lista capturada, usa la función anterior (calcular factorial) que recorre la lista de números y calcula el factorial de cada uno de ellos, 
# y regresa como resultado una lista con los factoriales de los números de la lista.
# Se imprime la lista original y la lista con los factoriales de los números capturados.

import os

def lee_arreglo():
    arreglo = input("Dame los números: ")
    n = list(map(int, arreglo.split()))
    return n

def calcula_factorial(num):
    if num == 0 or num == 1:
        return 1
    m = 1
    for i in range(2, num + 1):
        m *= i
    return m

def recibe_lista(lista):
    return [calcula_factorial(num) for num in lista]

#Programa principal
os.system("cls")

nums = lee_arreglo()
suma = recibe_lista(nums)

print("La lista de números original                     : ", nums)
print("La lista con las suma de dígitos de los números  : ", suma)
