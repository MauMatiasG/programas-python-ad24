# Calcular el número mayor de una serie de números introducidos por el teclado, 
# el proceso se detiene al introducir 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system("cls")

    print("Imprime el numero mayor de una serie de numeros introducidos")

    mayor = 0
    
    while True:
        numero_ingresado = int(input("Introduce un numero (0 para detener) "))
        
        if mayor == 0 or numero_ingresado > mayor:
            mayor = numero_ingresado

        if numero_ingresado == 0:
            print(f"\nEl numero mayor fue: {mayor}")
            break

    if input("\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado ...")
