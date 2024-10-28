# Programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos regrese la suma de números pares o impares en el rango de números especificados.
# El programa deberá mostrar un menú con las opciones correspondientes y llamara a la función según la opción seleccionada.

import os

def pares_impares(lim1, lim2, Le):
    if Le == 'P':
        return sum(i for i in range(lim1, lim2 + 1) if i % 2 == 0)
    elif Le == 'I':
        return sum(i for i in range(lim1, lim2 + 1) if i % 2 != 0)
    else:
        return "Error, introduce unicamente P o I"

#Programa principal

os.system("cls")

lim1 = int(input("De donde ? "))
lim2 = int(input("Hasta donde ? "))
Le = input("Pares o impares (P/I) ? ")
n = pares_impares(lim1, lim2, Le)

print("La suma es : ", n)




