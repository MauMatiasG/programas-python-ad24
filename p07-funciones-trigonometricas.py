# Uso de las funciones trigonometricas en python

import math

print("Calculo de las funcines trigonometricas")
print("Dame un angulo : ")

angulo = int(input())
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)

salida = ("Resumen de funciones\n"
f"El seno es {seno}\n"
f"El coseno es {coseno}\n"
f"La tangente es {tangente}\n"
f"El angulo {angulo} en radianes equivale a {grados}\n")

print(salida)


