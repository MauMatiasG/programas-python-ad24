# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos

import math as mt
import os

os.system("cls")

print("Calcula el tiempo en dias, minutos y segundos\n")

horas = float(input("Dame el total de horas "))

d = horas // 24
res = horas % 24
m = horas * 60
s = m * 60

print(f"Dias: {d} con {res} Horas restantes")
print("Minutos: ", m)
print("Segundos: ",s)
