# Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
# Se crea una función que suma los dígitos individuales de un número (ya la hicimos en clase)
# Se crea una función que recibe las lista capturada, usa la función anterior (suma dígitos) y recorre la lista de números y suma sus dígitos, y regresa una lista con las sumas de tos dígitos de los números de la lista.
# Se imprime la lista original y la lista con las sumas de los dígitos de los números capturados.

import os

def lee_arreglo():
    arreglo = input("Dame los numeros: ")
    return [int(num) for num in arreglo.split()]

def suma(num):
    suma = 0
    while num > 0:
        suma += num %10
        num //=10
    return suma

def suma_lista(lista):
    sum = []
    for num in lista:
        sum.append(suma(num))
    return sum

#Programa principal

os.system("cls")

nums = lee_arreglo()
suma_digitos = suma_lista(nums)

print("La lista de números original                     : ", nums)
print("La lista con las suma de dígitos de los números  : ", suma_digitos)