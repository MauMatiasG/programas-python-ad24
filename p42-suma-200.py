# Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, 
# luego mostrar cuantos números fueron introducidos y la suma de estos. 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os, random

while(True):
    
    os.system("cls")
    print("Imprime la suma y la cantidad de numeros introducidos cuando la suma de >= 200")
    numeros_introducidos = 0
    s = 0
    while True:
        num = int(input("Introduce un numero "))
        numeros_introducidos += 1
        s = s + num

        if s >= 200:
            print(f"\nLa suma es {s}")
            print(f"\nSe introdujeron un total de {numeros_introducidos} numeros")
            break

    if input("\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado ...")