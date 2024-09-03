# Realizar un programa que pida un número entre 1 y 10 y 
# muestre su equivalente en número romano ( I, II, III, IV, V, VI, VII, VIII, IX, X). 
# Si el número no esta en el rango solicitado que mande un mensaje de error.

import os; os.system("cls")

print("Muestra el equivalente en numero romano de un numero")

print("Introduce un numero entero del 1 al 10")
n1 = int(input())

if n1 == 1:
    print("El numero romano es: I")
elif n1 == 2:
    print("El numero romano es: II")
elif n1 == 3:
    print("El numero romano es: III")
elif n1 == 4:
    print("El numero romano es: IV")
elif n1 == 5:
    print("El numero romano es: V")
elif n1 == 6:
    print("El numero romano es: VI")
elif n1 == 7:
    print("El numero romano es: VII")
elif n1 == 8:
    print("El numero romano es: VIII")
elif n1 == 9:
    print("El numero romano es: IX")
elif n1 == 10:
    print("El numero romano es: X")
else:
    print("Numero invalido")

print("\nProceso terminado ... ")