# Imprime numerss pares de 2 a n y su suma


import os; os.system("cls")

print("Imprime numeros pares de 2 a n y su suma")

n = int(input("\nDame número: "))
s = 0

for x in range(2, n+1, 2):
    print(x,end=" ")
    s = s + x
print(f"\nLa suma es = {s}")
