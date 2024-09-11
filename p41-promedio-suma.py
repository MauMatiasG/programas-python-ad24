# Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
# además deberá contar cuantos números se introdujeron. 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system("cls")

    print("Imprime la suma, el promedio y la cantidad de una serie de numeros introducidos")

    stop = 0
    numeros_introducidos = 0
    s = 0
    while True:
        numero_ingresado = int(input("\nIntroduce un numero (0 para detener) "))
        numeros_introducidos += 1
        s = s + numero_ingresado

        if numero_ingresado == stop:
            numeros_introducidos -= 1
            print(f"\nLa suma es {s}")
            print(f"\nEl promedio es {s/numeros_introducidos}")
            print(f"\nSe introdujeron un total de {numeros_introducidos} numeros")
            break

    if input("\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado ...")
