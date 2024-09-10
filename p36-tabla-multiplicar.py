# Imprime la tabla de multiplicar que el usuario pida hasta donde la pida

import os

while(True):
    os.system("cls")
    t = int(input("Que tabla quieres ? "))
    n = int(input("Hasta donde ? "))

    c = 1
    while c <= n:
        print(f"{t} x {c} = {t*c}")
        c+=1

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado")
