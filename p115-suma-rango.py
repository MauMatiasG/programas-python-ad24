# Suma rango valores

import os

def sumarango(ini, fin):
    s = 0
    for i in range(ini, fin+1):
        s += i
    return s

#Principal
os.system("cls")
while True:
    ini = int(input("Dame el valor inicial : "))
    fin = int(input("Dame el valor fina    : "))
    if fin>ini: break
    
print(f"La suma del rango de valores es ", sumarango(ini, fin))