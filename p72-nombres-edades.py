# Procesa nombres y edades en dos listas paralelas, el usuario introduce los datos

import os; os.system("cls")

nombres= []
edades = []

while True:
    nombre = input("Nombre : ")
    if nombre !="*":
        nombres.append(nombre)
        edad = int(input("Edad : "))
        edades.append(edad)
    else:
        break

print("Nombres : ", nombres)
print("Edades  : ", edades)

print("Mayores de edad : ")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"Nombre = {nombres[i]}, Edad = {edades[i]}")

pos = edades.index( max(edades))
print(f"El alumno {nombres[pos]}, con edad de {edades[pos]} es el mayor de todos")