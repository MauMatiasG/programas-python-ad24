# Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, 
# si no lo son (1,4,6) mandar mensaje de error.

import os; os.system("cls")

print("Verifica si tres numeros son consecutivos")

print("Introduce tres numeros enteros, separados por un enter")
n1,n2,n3 = int(input()), int(input()), int(input())

n4 = n1 + 1
n5 = n2 + 1

n6 = n1 - 1
n7 = n2 - 1

if n2 == n4 and n3 == n5:
    print(f"\nLos numeros ({n1}, {n2}, {n3}) son consecutivos")
elif n2 == n6 and n3 == n7:
    print(f"\nLos numeros ({n1}, {n2}, {n3}) son consecutivos")
else:
    print(f"\n Los numeros ({n1}, {n2}, {n3}) no son consecutivos")

print("\nProceso terminado ... ")