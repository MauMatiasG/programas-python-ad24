# Llenar una lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
# Calcular e imprimir la suma y promedio de los números
# Mostrar los números que son divisibles entre 3 y sumarlos
# Pedir un elemento a buscar en la lista original y decir si esta y en que posición

import os, random; os.system("cls")

A = []
B = []

n2 = suma2 = suma = promedio = 0
n = 1

nu = int(input("Cuantos numeros impares ? "))

for x in range(nu):
    A.append(n)
    if n%3 == 0:
        n2 = n
        B.append(n)
        suma2 = suma2 + n2
    n = n+2
    suma += n -2
promedio = suma / len(A)

print(f"\nLos primeros {nu} numeros impares son :", A)
print("La suma es                                 :", suma)
print("El promedio es es                          :", promedio)
print("Los numeros que son divisibles entre 3 son :", B)
print("La suma de los divisibles entre 3 es       :", suma2)

bus = int(input("\nNumero a buscar en la lista original ? "))
if bus in A:
    pos = A.index(bus)
    print(f"El elemento buscado SI esta en la lista original y se encuentra en la posicion {pos} comenzando desde la posicion 0")
else:
    print("El elemento buscado NO esta en la lista original")





