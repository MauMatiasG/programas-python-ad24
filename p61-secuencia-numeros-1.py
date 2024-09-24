# Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee

import os; os.system("cls")

print("Imprime la secuencia de números mostradros en renglones")

n = int(input("\nDame número ? "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()