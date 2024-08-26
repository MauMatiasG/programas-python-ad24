# Dividir en cifras un numero entero

import math 

print("Dividir en unidades, decenas y centenas un numero entero")
numero = int(input("Dame un número de 3 cifras "))

centenas = math.trunc( numero / 100)
decenas = math.trunc( (numero-centenas * 100) / 10)
unidades = numero - (centenas * 100 + decenas * 10)

print(f"centenas: {centenas}, decenas: {decenas}, unidades: {unidades} ")
