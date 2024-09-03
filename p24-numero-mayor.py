#  Dados tres números enteros, verificar cual es el mayor, 
# ej: 10, 9 8, el mayor es 10, 11, 30, -1 el mayor es 30 

import os; os.system("cls")

print("Verifica el numero mayor")

print("Introduce tres numeros enteros, separados por un enter")
n1,n2,n3 = int(input()), int(input()), int(input())

if n1 > n2 and n1 > n3:
    print(f"De los numeros ({n1}, {n2}, {n3}) el mayos es: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"De los numeros ({n1}, {n2}, {n3}) el mayos es: {n2}")
elif n3 > n1 and n3 > n1:
    print(f"De los numeros ({n1}, {n2}, {n3}) el mayos es: {n3}")

print("\nProceso terminado ... ")