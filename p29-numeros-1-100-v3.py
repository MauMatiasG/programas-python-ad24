# Imprime numeros del 1 a n, en incrementos de p, usando while

import os; os.system("cls")

print("\nImprime numeros del 1 a n, en incrementos de p\n")

c = 1

n = int(input("Hasa donde deseas llegar ? "))
p= int(input("En incrmendto de ? "))

while c <= n:
    print(c, end=" ")
    c = c + p

print("\nCiclo terminado")
