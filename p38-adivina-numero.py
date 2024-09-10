# El usuario adivina un numero entero entre el 1 y 100

import os, random

while(True):
    os.system("cls")

    numero_secreto = random.randint(1,100)
    intentos = 0
    while True:
        numero_ingresado = int(input("Adivina el numero secreto (1-100) "))
        intentos += 1
        if numero_ingresado == numero_secreto:
            print(f"\nFelicidades adivinaste en {intentos} intentos")
            break
        elif numero_ingresado < numero_secreto:
            print("El numero secreto es mayor")
        else:
            print("El numero secreto es menor")
    

    if input("\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado ...")
