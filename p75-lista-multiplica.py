# Leer dos listas con 5 elementos. Multiplica las listas y guárdalos en una tercera lista. Imprime las tres listas

import os; os.system("cls")

A = []
B = []
C = []

print("Leer lista A")
for i in range(5):
    n = int(input(f"A[{i}] = ")) 
    A.append(n)
print(A)

print("Leer lista B")
for i in range(5):
    n = int(input(f"B[{i}] = ")) 
    B.append(n)
print(B)

print("\nMultiplicacion de listas C = A * B")
for i in range(5):
    C.append(A[i] * B[i])
print("Lista A", A)
print("Lista B", B)
print("Lista C", C) 