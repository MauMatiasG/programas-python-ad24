# Funcion que suma los digitos de un numero
# 1971 = 18

import os

def sumadigitos(n):
    suma = 0
    while n != 0:
        dig = n % 10
        suma += dig
        n = n//10
    return suma

#Principal
os.system("cls")
n = int(input("Dame un numero entero y te regreso la suma de sus digitos ? "))
print("\nLa suma de los digitos es ", sumadigitos(n))
