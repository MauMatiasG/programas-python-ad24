# Calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados

import math as mt
import os

os.system("cls")

print("Calcula la hipotenusa de un triángulo rectángulo\n")

longlado1 = float(input("Dame la longitud del primer lado del triangulo "))
longlado2 = float(input("Dame la longitud del segundo lado del triangulo "))

hipotenusa = mt.sqrt( ( longlado1 * longlado1 ) + ( longlado2 * longlado2 ) )

print(f"La longitud de la hipotenusa del triangulo es: {hipotenusa:.3f}")
