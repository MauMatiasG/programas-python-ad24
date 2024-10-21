# Tabla de multiplicar usando funcion

import os

def tabla_multiplicar(t, n):
    for i in range(1, n+1):
        print(f"{t} x {i} = {t*i}")
    print("\n")

#Principal
os.system("cls")
#tabla_multiplicar(10,5)
#tabla_multiplicar(8,7)
t = int(input("Que tabla quieres "))
n = int(input("Hasta donde       "))
tabla_multiplicar(t,n)