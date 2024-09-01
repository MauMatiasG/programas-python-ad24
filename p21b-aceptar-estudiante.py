# Aceptar estudiante en base a cierto criterios

import os; os.system("cls")

print("Universidad Patito SA de CV\n")

nombre = input("Dame tu nombre > ")
print("Dame 2 calificaciones > ")
c1, c2 = int(input()), int(input())

if  c1 < 8 or c2 < 8:
    print("Solo aceptamos alumnos con calificaciones mayores a 8")
else:
    edad = int(input("Dame tu edad > "))
    if edad < 18:
        print("Solo aceptamos mayores de 18")
    else:
        print(f"{nombre} bienvenid@ a la Universidad Patito, tu edad {edad} y calificaciones {c1} y {c2} lo permien")