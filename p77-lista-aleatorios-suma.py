# Generar 2 listas de 10 números aleatorios
# Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares
# Imprime las 3 listas

import os, random; os.system("cls")

A = []
B = []
C = []

print("Generando aleatorios ...")
for x in range(10):
    A.append(random.randint(1,10))
    B.append(random.randint(1,10))
print("A = ", A)
print("B = ", B)
print()

print("Suma de listas C = A + B, solo elementos de cada lista que ambos son impares")
for i in range(10):
    if A[i] %2 != 0 and B[i] %2 !=0:
        C.append(A[i] + B[i])
print(C) 