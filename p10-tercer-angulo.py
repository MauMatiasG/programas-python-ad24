# Dados dos ángulos de un triángulo, calcular el 3er ángulo

import math as mt
import os

os.system("cls")

print("Calcula el 3er angulo de un triangulo\n")

angulo1 = float(input("Dame el primer angulo "))
angulo2 = float(input("Dame el segundo angulo "))

angulo3 = 180 - (angulo1 + angulo2)

print("El 3er Angulo es : ", angulo3)
