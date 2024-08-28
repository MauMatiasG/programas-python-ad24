# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte

import math as mt
import os

os.system("cls")

print("Calcula el numero de la suerte\n")

n = int(input("Dame tu año de nacimineto "))

m = n // 1000
c = (n - ( m *1000 ) ) // 100
d = ( n - ( m * 1000 + c *100) ) // 10
u = ( n -( m * 1000  + c * 100 + d * 10 ))

numsuerte = m + c + d + u

print("\nEl numero en cifras individuales es\n")
print("Uniddes de millar:", m)
print("Centenas:", c)
print("Decenas:", d)
print(f"Unidades: {u}\n")

print(f"Tu numero de la suerte es: {numsuerte}")


 