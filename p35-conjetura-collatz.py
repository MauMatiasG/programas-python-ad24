# Calcula e imprime los numeros de la conjetura de collatz

import os

while (True):

    os.system("cls")
    num = int(input("Dame un entero positivo ? "))

    while num !=1:
        print(num, end=" ")
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1 
    print(num, end=" ")

    if input("\nDeseas continuar (S/N) ").upper().startswith("N"): break
    
print("\nProceso terminado")