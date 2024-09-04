# Imprime numeros hasta llegar a una suma de 100 

import os; os.system("cls")

print("\nImprime numeros hasta llegar a una suma de 100\n")

c = 0
s = 0

while c < 300:
    c = c + 1 
    s = s + c
    print(c, end = " ")
    if s >= 10000:
        print("\n")
        break

print(f"\nLa suma es {s}, sumando {c} numeros ")

