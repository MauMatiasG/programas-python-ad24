# Aceptar un estudiante en base a su edad y dos calificaciones

import os; os.system("cls")

print("Universidad Patito SA de CV")
print("Aceptar un estudiante base a su edad y dos calificaciones\n")

nombre = input("Dame el nombre ? ")
edad = int(input("Dame la edad ? "))

if edad >= 18:
    print("Dame 2 calificaciones separadas por enter ? ")
    c1, c2 = int(input()), int(input())
    if c1 >= 8 and c2 >= 8:
        print(f"{nombre} bienvenid@ a la Universidad Patito, tu edad {edad} y calificaciones {c1} y {c2} lo permien")
    else:
         print("\nSolo aceptamos alumnos con calificacoines mayores o iguales a 8")
else: 
    print("\nSolo aceptamos a mayores de edad") 
      
print("\nGracias por utilizar este programa ...")