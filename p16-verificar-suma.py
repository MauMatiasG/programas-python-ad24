# Verifica si la suma de 2 numeros es igual a un tercero

import os; os.system("cls")

print("Verifica si la suma de 2 numeros es igual a un tercero\n")

n1 = int(input("Dame numero 1 ? "))
n2 = int(input("Dame numero 2 ? "))
n3 = int(input("Dame numero 3 ? "))

if n1 + n2 == n3 :
    print("\nSon iguales")
else :
    print("\nSon diferentes")

print("\nProceso terminado ...")
