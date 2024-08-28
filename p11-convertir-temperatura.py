# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit

import math as mt
import os

os.system("cls")

print("Calcula la temperatura en grados Farenheit\n")

celcius = float(input("Dame la temperatura en grados Celcius "))

farenheit = ( ( celcius * ( 9/5 ) ) + 32 )

print(f"\nLa temperatura en grados Farenheit es: {farenheit}")
