# Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:

import os; os.system("cls")

print("Imprime la secuencia de términos armónicos y su suma")

n = int(input("\n¿Cuántos terminos? "))
s = 0

for x in range (1, n+1, 1):
    if x == 1:
        print(1,end="")
    else:
        print(f" + 1/{x}!",end="")
    s = s + (1/x)
print(f"\nSuma: {s}")