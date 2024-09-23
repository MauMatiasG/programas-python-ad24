# Calcula el factorial de un numero

import os; os.system("cls")

n = int(input("Dame un numero ? "))

f = 1

print(f"{n}! = ", end=" ")

for i in range(1, n+1):
    f = f * i 
    print(f"{i} {"x" if i!=n else ""}", end=" ")

print(f"= {f}")