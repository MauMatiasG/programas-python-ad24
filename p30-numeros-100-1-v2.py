# Imprime los numeros de n a 1 

import os; os.system("cls")

print("\nImprime los numeros de 100 a 1 \n")

n= int(input("Desde donde ? "))

c = n

while c >= 1:
    print(c, end=" ")
    c = c - 1
    
print("\nCiclo terminado")
