# Verificar si la suma de dos numeros es igual a un tercero

import os; os.system("cls")

print("Verificar si la suma de dos numeros es igual a un tercero\n")
print("Dame 3 numeros enteros separados por espacio ? ")
n1, n2, n3 = input().split()
n1, n2, n3 =[ int(n1), int(n2), int(n3) ]

if n1 + n2 == n3:
    print("n1 + n2 = n3")
elif n1 + n3 == n2:
    print("n1 + n3 = n2")
elif n2 + n3 == n1:
    print("n2 + n3 = n1")
else: 
    print("Posiblemente son iguales")

