# Verificar si un numero es positivo, negativo o es cero

import os; os.system("cls")

print("Verificar si un numero es positivo, negativo o es cero\n")

numero = int(input("Dame un numero entero ? "))

if numero > 0:
    print("\nEl numero es positivo")

if numero < 0:
    print("\nEl numero es negativo")

if numero == 0:
    print("\nEl numero es cero")

print("\nProceso terminado ...")