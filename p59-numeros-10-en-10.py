# Imprime los numeros de 1 a n de 10 en 10

import os; os.system("cls")

print("Imprime los numeros de 1 a n de 10 en 10")
n = int(input("\nDame número: "))

for x in range (1, n ,10):
    print (x, end=" ")