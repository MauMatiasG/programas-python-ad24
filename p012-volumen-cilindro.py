# Calcular el volumen de un cilindro dado su radio y altura

import math as mt
import os

os.system("cls")

print("Calcula el volumen de un cilindro\n")

Radio =  float(input("Dame el Radio del cilindro "))
Altura = float(input("Dame la Alura del cilindro "))

Volumen = mt.pi * ( Radio * Radio ) * Altura

print(f"El Volumen del cilindro es : {Volumen:.3f}")