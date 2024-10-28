# Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
# Crear una función para cada una de las siguientes estadísticas (poblacional):
# Mayor, Menor, Media, Varianza, Desviación estánda
# Se muestran los resultados de cada operación.

import os, math

def lee_arreglo():
    nums = input("Dame numeros: ").split()
    arreglo = [int(num) for num in nums]
    return arreglo

def mayor(lista):
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
    return max

def menor(lista):
    min = lista[0]
    for num in lista:
        if num < min:
            min = num
    return min

def media(lista):
    total = sum(lista)
    return total / len(lista)

def varianza(lista):
    med = media(lista)
    diferencia = sum((x - med) ** 2 for x in lista)
    return diferencia / len(lista)

def desviacion_estandar(lista):
    return math.sqrt(varianza(lista))


#Programa principal
os.system("cls")

nums = lee_arreglo()
med = media(nums)
max = mayor(nums)
min = menor(nums)
vari = varianza(nums)
desviacion = desviacion_estandar(nums)

print("Lista de números     :", nums)
print(f"La media             : {med:.3f}")
print("Mayor de los datos   :", max)
print("Menor de los datos   :", min)
print(f"Varianza             : {vari:.3f}")
print(f"Desviación estándar  : {desviacion:.3f}")