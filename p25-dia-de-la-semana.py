# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 
# 1 es domingo, 2 es lunes y así hasta 7 es viernes. 
# Si el número no está en el rango especificado, mostrar un mensaje de error. 

import os; os.system("cls")

print("Muestra el dia de la semana correspondiente al numero")

print("Introduce un numero entero del 1 al 7")
n1 = int(input())

if n1 == 1:
    print("El dia de la semana es: Domingo")
elif n1 == 2:
    print("El dia de la semana es: Lunes")
elif n1 == 3:
    print("El dia de la semana es: Martes")
elif n1 == 4:
    print("El dia de la semana es: Miercoles")
elif n1 == 5:
    print("El dia de la semana es: Jueves")
elif n1 == 6:
    print("El dia de la semana es: Viernes")
elif n1 == 7:
    print("El dia de la semana es: Sabado")
else:
    print("Dia invalido")

print("\nProceso terminado ... ")